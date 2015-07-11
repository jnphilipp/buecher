from django.db import models
from django.template.defaultfilters import slugify
from links.models import Link
from persons.models import Person
from series.models import Series

class TextFieldSingleLine(models.TextField):
    pass

class Book(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True)
    title = TextFieldSingleLine(unique=True)
    authors = models.ManyToManyField(Person, related_name='books', blank=True)

    series = models.ForeignKey(Series, blank=True, null=True)
    volume = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            orig = Book.objects.get(pk=self.id)
            if orig.title != self.title:
                self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return '%s%s%s' % (self.title, '' if self.authors.count() == 0 else ' - %s' % ', '.join([str(a) for a in self.authors.all()]), ' (%s #%g)' % (self.series, self.volume) if self.series else '')

    class Meta:
        ordering = ('title',)
