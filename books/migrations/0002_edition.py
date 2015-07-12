# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
        ('languages', '0001_initial'),
        ('links', '0001_initial'),
        ('bindings', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isbn', models.CharField(null=True, max_length=13, blank=True)),
                ('asin', models.CharField(null=True, max_length=10, blank=True)),
                ('published_on', models.DateField(null=True, blank=True)),
                ('cover_image', models.ImageField(null=True, blank=True, upload_to='books')),
                ('bibtex', models.TextField(null=True, blank=True)),
                ('binding', models.ForeignKey(blank=True, null=True, to='bindings.Binding', related_name='editions')),
                ('book', models.ForeignKey(to='books.Book', related_name='editions')),
                ('languages', models.ManyToManyField(to='languages.Language', related_name='editions', blank=True)),
                ('links', models.ManyToManyField(to='links.Link', related_name='editions', blank=True)),
                ('publisher', models.ForeignKey(blank=True, null=True, to='publishers.Publisher', related_name='editions')),
            ],
            options={
                'verbose_name': ' edition',
                'ordering': ('book',),
            },
        ),
    ]
