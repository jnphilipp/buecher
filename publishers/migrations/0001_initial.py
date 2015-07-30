# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import publishers.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=2048, unique=True)),
                ('name', publishers.models.TextFieldSingleLine(unique=True)),
                ('links', models.ManyToManyField(to='links.Link', blank=True, related_name='publishers')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': ' publisher',
            },
        ),
    ]
