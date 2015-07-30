# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import persons.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=2048, unique=True)),
                ('first_name', persons.models.TextFieldSingleLine()),
                ('last_name', persons.models.TextFieldSingleLine()),
                ('links', models.ManyToManyField(related_name='persons', to='links.Link', blank=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
                'verbose_name': ' person',
            },
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('last_name', 'first_name')]),
        ),
    ]
