# -*- coding: utf-8 -*-

import os
import shutil

from bindings.models import Binding
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from languages.models import Language
from links.models import Link
from persons.models import Person
from publishers.models import Publisher
from series.models import Series

def get_ebook_path(obj, filename):
    name = slugify('%s%s' % (obj.edition.book.title, '' if obj.edition.book.authors.count() == 0 else ' - %s' % ', '.join([str(a) for a in obj.edition.book.authors.all()])))
    return os.path.join('books', str(obj.edition.id), name + os.path.splitext(filename)[1])

class TextFieldSingleLine(models.TextField):
    pass

class Book(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True)
    title = TextFieldSingleLine(unique=True)
    authors = models.ManyToManyField(Person, related_name='books', blank=True)

    series = models.ForeignKey(Series, related_name='books', blank=True, null=True)
    volume = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            orig = Book.objects.get(pk=self.id)
            if orig.title != self.title:
                self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def to_json(self):
        data = {'title':self.title}
        if self.authors.all():
            data['authors'] = [author.to_json() for author in self.authors.all()]
        if self.series:
            data['series'] = self.series.name
            data['volume'] = self.volume
        return data

    def __str__(self):
        return '%s%s%s' % (self.title, '' if self.authors.count() == 0 else ' - %s' % ', '.join([str(a) for a in self.authors.all()]), ' (%s #%g)' % (self.series, self.volume) if self.series else '')

    class Meta:
        ordering = ('series', 'volume', 'title')
        verbose_name = ' book'

class Edition(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey(Book, related_name='editions')
    isbn = models.CharField(max_length=13, blank=True, null=True)
    asin = models.CharField(max_length=10, blank=True, null=True)
    published_on = models.DateField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='books', blank=True, null=True)

    publisher = models.ForeignKey(Publisher, related_name='editions', blank=True, null=True)
    binding = models.ForeignKey(Binding, related_name='editions', blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='editions', blank=True)
    links = models.ManyToManyField(Link, related_name='editions', blank=True)
    bibtex = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('edition', args=[self.book.slug, self.id])

    def save(self, *args, **kwargs):
        super(Edition, self).save()
        if self.cover_image.name:
            self.cover_image = self.move_image()
            super(Edition, self).save()

    def move_image(self):
        save_name = os.path.join('books', str(self.id), 'cover%s' % os.path.splitext(self.cover_image.name)[1])
        current_path = os.path.join(settings.MEDIA_ROOT, self.cover_image.path)
        new_path = os.path.join(settings.MEDIA_ROOT, save_name)

        if os.path.exists(current_path):
            if not os.path.exists(os.path.dirname(new_path)):
                os.makedirs(os.path.dirname(new_path))

            shutil.move(current_path, new_path)

        return save_name

    def __str__(self):
        return str(self.book)

    class Meta:
        ordering = ('book',)
        verbose_name = ' edition'

class EBookFile(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    edition = models.ForeignKey(Edition, related_name='ebookfiles')
    ebook = models.FileField(upload_to=get_ebook_path, max_length=4096)

    def __str__(self):
        return os.path.basename(self.ebook.name)

    class Meta:
        ordering = ('edition',)
        verbose_name = ' ebook file'
