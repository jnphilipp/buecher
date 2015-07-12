from django.db import models
from django.template.defaultfilters import slugify
from links.models import Link

class TextFieldSingleLine(models.TextField):
    pass

class Person(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True)
    first_name = TextFieldSingleLine()
    last_name = TextFieldSingleLine()
    links = models.ManyToManyField(Link, related_name='persons', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('%s %s' % (self.first_name, self.last_name))
        else:
            orig = Person.objects.get(pk=self.id)
            if orig.first_name != self.first_name or orig.last_name != self.last_name:
                self.slug = slugify('%s %s' % (self.first_name, self.last_name))
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
        unique_together = ('last_name', 'first_name')
        verbose_name = ' person'
