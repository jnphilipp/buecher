# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_bibtex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binding',
            name='name',
            field=books.models.TextFieldSingleLine(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=books.models.TextFieldSingleLine(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=books.models.TextFieldSingleLine(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=books.models.TextFieldSingleLine(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=books.models.TextFieldSingleLine(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=books.models.TextFieldSingleLine(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=books.models.TextFieldSingleLine(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=books.models.TextFieldSingleLine(),
            preserve_default=True,
        ),
    ]
