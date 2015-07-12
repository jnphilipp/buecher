# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_edition'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBookFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ebook', models.FileField(max_length=4096, upload_to=books.models.get_ebook_path)),
                ('edition', models.ForeignKey(related_name='ebookfiles', to='books.Edition')),
            ],
            options={
                'verbose_name': ' ebook file',
                'ordering': ('edition',),
            },
        ),
    ]
