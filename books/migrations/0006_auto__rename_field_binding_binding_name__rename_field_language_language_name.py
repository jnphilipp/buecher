# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename field 'binding' to 'name'
        db.rename_column('books_binding', 'binding', 'name')

        # Rename field 'language' to 'name'
        db.rename_column('books_language', 'language', 'name')


    def backwards(self, orm):
        # Rename field 'name' to 'binding'
        db.rename_column('books_binding', 'name', 'binding')

        # Rename field 'name' to 'language'
        db.rename_column('books_language', 'name', 'language')


    models = {
        'books.binding': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Binding'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'asin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['books.Person']"}),
            'binding': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['books.Binding']"}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '13'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['books.Language']"}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'published_on': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['books.Publisher']"}),
            'purchased_on': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'read_on': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['books.Series']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'})
        },
        'books.ebookfile': {
            'Meta': {'object_name': 'EBookFile'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Book']"}),
            'ebook_file': ('django.db.models.fields.files.FileField', [], {'max_length': '4096'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'books.language': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'books.person': {
            'Meta': {'ordering': "('lastname', 'firstname')", 'unique_together': "(('firstname', 'lastname'),)", 'object_name': 'Person'},
            'firstname': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {})
        },
        'books.publisher': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'books.series': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'books.url': {
            'Meta': {'object_name': 'Url'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['books']