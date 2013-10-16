# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EBookFile.ebook_file'
        db.alter_column(u'books_ebookfile', 'ebook_file', self.gf('django.db.models.fields.files.FileField')(max_length=4096))

    def backwards(self, orm):

        # Changing field 'EBookFile.ebook_file'
        db.alter_column(u'books_ebookfile', 'ebook_file', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'books.binding': {
            'Meta': {'ordering': "('binding',)", 'object_name': 'Binding'},
            'binding': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['books.Person']", 'null': 'True', 'blank': 'True'}),
            'binding': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Binding']", 'null': 'True', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['books.Language']", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'published_on': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Publisher']", 'null': 'True', 'blank': 'True'}),
            'purchased_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'read_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Series']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'books.ebookfile': {
            'Meta': {'object_name': 'EBookFile'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Book']"}),
            'ebook_file': ('django.db.models.fields.files.FileField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'books.language': {
            'Meta': {'ordering': "('language',)", 'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.TextField', [], {})
        },
        u'books.person': {
            'Meta': {'ordering': "('lastname', 'firstname')", 'object_name': 'Person'},
            'firstname': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {})
        },
        u'books.publisher': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Publisher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'books.series': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Series'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['books']