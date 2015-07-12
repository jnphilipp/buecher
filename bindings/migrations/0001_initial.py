# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bindings.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', bindings.models.TextFieldSingleLine(unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': ' binding',
            },
        ),
    ]
