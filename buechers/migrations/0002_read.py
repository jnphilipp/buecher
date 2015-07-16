# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_ebookfile'),
        ('buechers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started', models.DateField(verbose_name=' date started', null=True, blank=True)),
                ('finished', models.DateField(verbose_name=' date finished', null=True, blank=True)),
                ('edition', models.ForeignKey(to='books.Edition')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' read',
                'ordering': ('user', 'edition'),
            },
        ),
    ]
