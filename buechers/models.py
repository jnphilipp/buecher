# -*- coding: utf-8 -*-

from books.models import Edition
from django.conf import settings
from django.db import models
from units.models import Unit

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
