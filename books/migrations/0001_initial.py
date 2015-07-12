# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', books.models.TextFieldSingleLine(unique=True)),
                ('volume', models.FloatField(blank=True, default=0)),
                ('authors', models.ManyToManyField(related_name='books', blank=True, to='persons.Person')),
                ('series', models.ForeignKey(null=True, to='series.Series', blank=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': ' book',
            },
        ),
    ]
