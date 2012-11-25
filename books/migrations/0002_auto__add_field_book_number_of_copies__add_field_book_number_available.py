# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.number_of_copies'
        db.add_column('books_book', 'number_of_copies',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Book.number_available'
        db.add_column('books_book', 'number_available',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.number_of_copies'
        db.delete_column('books_book', 'number_of_copies')

        # Deleting field 'Book.number_available'
        db.delete_column('books_book', 'number_available')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'dra': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'grade_level': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Level']"}),
            'number_available': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'number_of_copies': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        'books.level': {
            'Meta': {'object_name': 'Level'},
            'dra': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'grade_level': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'guided_reading': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['books']