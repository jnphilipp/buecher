# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('books_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.TextField')()),
            ('lastname', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('books', ['Person'])

        # Adding model 'Publisher'
        db.create_table('books_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('books', ['Publisher'])

        # Adding model 'Binding'
        db.create_table('books_binding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('binding', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('books', ['Binding'])

        # Adding model 'Language'
        db.create_table('books_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('books', ['Language'])

        # Adding model 'Series'
        db.create_table('books_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('books', ['Series'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13, blank=True)),
            ('asin', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('published_on', self.gf('django.db.models.fields.DateField')()),
            ('purchased_on', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('read_on', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('binding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Binding'], null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'], null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Series'], null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('books', ['Book'])

        # Adding M2M table for field languages on 'Book'
        db.create_table('books_book_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('language', models.ForeignKey(orm['books.language'], null=False))
        ))
        db.create_unique('books_book_languages', ['book_id', 'language_id'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('books_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('person', models.ForeignKey(orm['books.person'], null=False))
        ))
        db.create_unique('books_book_authors', ['book_id', 'person_id'])

        # Adding model 'EBookFile'
        db.create_table('books_ebookfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ebook_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Book'])),
        ))
        db.send_create_signal('books', ['EBookFile'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('books_person')

        # Deleting model 'Publisher'
        db.delete_table('books_publisher')

        # Deleting model 'Binding'
        db.delete_table('books_binding')

        # Deleting model 'Language'
        db.delete_table('books_language')

        # Deleting model 'Series'
        db.delete_table('books_series')

        # Deleting model 'Book'
        db.delete_table('books_book')

        # Removing M2M table for field languages on 'Book'
        db.delete_table('books_book_languages')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('books_book_authors')

        # Deleting model 'EBookFile'
        db.delete_table('books_ebookfile')


    models = {
        'books.binding': {
            'Meta': {'object_name': 'Binding'},
            'binding': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['books.Person']", 'null': 'True', 'blank': 'True'}),
            'binding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Binding']", 'null': 'True', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['books.Language']", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'published_on': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Publisher']", 'null': 'True', 'blank': 'True'}),
            'purchased_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'read_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Series']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'books.ebookfile': {
            'Meta': {'object_name': 'EBookFile'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Book']"}),
            'ebook_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'books.language': {
            'Meta': {'ordering': "('language',)", 'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.TextField', [], {})
        },
        'books.person': {
            'Meta': {'ordering': "('lastname', 'firstname')", 'object_name': 'Person'},
            'firstname': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {})
        },
        'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'books.series': {
            'Meta': {'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['books']