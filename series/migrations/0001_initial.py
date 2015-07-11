# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import series.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', series.models.TextFieldSingleLine(unique=True)),
            ],
            options={
                'verbose_name': 'series',
                'verbose_name_plural': 'series',
                'ordering': ('name',),
            },
        ),
    ]
