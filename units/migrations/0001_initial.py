# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import units.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', units.models.TextFieldSingleLine(unique=True)),
                ('symbol', units.models.TextFieldSingleLine(unique=True)),
                ('precision', models.PositiveIntegerField(default=2)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': ' unit',
            },
        ),
    ]
