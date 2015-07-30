# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import buechers.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_ebookfile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buechers', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=2048, unique=True)),
                ('name', buechers.models.TextFieldSingleLine()),
                ('books', models.ManyToManyField(to='books.Book', related_name='lists', blank=True)),
                ('editions', models.ManyToManyField(to='books.Edition', related_name='lists', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' list',
                'ordering': ('user', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([('user', 'name')]),
        ),
    ]
