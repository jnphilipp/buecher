# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import books.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('isbn', models.CharField(blank=True, max_length=13)),
                ('asin', models.CharField(blank=True, max_length=10)),
                ('price', models.FloatField(default=0)),
                ('published_on', models.DateField(blank=True, null=True)),
                ('purchased_on', models.DateField(blank=True, null=True)),
                ('read_on', models.DateField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='books')),
                ('volume', models.FloatField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EBookFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ebook_file', models.FileField(max_length=4096, upload_to=books.models.get_ebook_path)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
                'verbose_name': 'E-Book File',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
            ],
            options={
                'ordering': ('lastname', 'firstname'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('firstname', 'lastname')]),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='books.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='binding',
            field=models.ForeignKey(blank=True, null=True, to='books.Binding'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(blank=True, to='books.Language', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, to='books.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, to='books.Series'),
            preserve_default=True,
        ),
    ]
