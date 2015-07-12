# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import languages.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', languages.models.TextFieldSingleLine(unique=True)),
            ],
            options={
                'verbose_name': ' language',
                'ordering': ('name',),
            },
        ),
    ]
