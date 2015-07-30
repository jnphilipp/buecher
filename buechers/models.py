# -*- coding: utf-8 -*-

from books.models import Book, Edition
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from units.models import Unit

class TextFieldSingleLine(models.TextField):
    pass

class Profile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    default_unit = models.ForeignKey(Unit, blank=True, null=True)

    class Meta:
        ordering = ('user',)
        verbose_name = ' profile'

class Possession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    edition = models.ForeignKey(Edition)
    unit = models.ForeignKey(Unit)
    acquisition = models.DateField(verbose_name=' date of acquisition')
    price = models.FloatField(default=0)

    def __str__(self):
        return '%s - %s' % (self.user, self.edition)

    class Meta:
        ordering = ('user', 'edition')
        verbose_name = ' possession'

class Read(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    edition = models.ForeignKey(Edition)
    started = models.DateField(verbose_name=' date started', blank=True, null=True)
    finished = models.DateField(verbose_name=' date finished', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.user, self.edition)

    class Meta:
        ordering = ('user', 'edition')
        verbose_name = ' read'

class List(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=2048, unique=True)
    name = TextFieldSingleLine()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    books = models.ManyToManyField(Book, related_name='lists', blank=True)
    editions = models.ManyToManyField(Edition, related_name='lists', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('%s-%s' % (self.user.username, self.name))
        else:
            orig = List.objects.get(pk=self.id)
            if orig.name != self.name:
                self.slug = slugify('%s-%s' % (self.user.username, self.name))
        super(List, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.user, self.name)

    class Meta:
        ordering = ('user', 'name')
        unique_together = ('user', 'name')
        verbose_name = ' list'
