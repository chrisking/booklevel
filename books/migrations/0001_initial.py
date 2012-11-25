# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table('books_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guided_reading', self.gf('django.db.models.fields.CharField')(max_length='1')),
            ('grade_level', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('dra', self.gf('django.db.models.fields.CharField')(max_length='10')),
        ))
        db.send_create_signal('books', ['Level'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Level'])),
            ('grade_level', self.gf('django.db.models.fields.CharField')(max_length='10', null=True, blank=True)),
            ('dra', self.gf('django.db.models.fields.CharField')(max_length='10', null=True, blank=True)),
        ))
        db.send_create_signal('books', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table('books_level')

        # Deleting model 'Book'
        db.delete_table('books_book')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'dra': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'grade_level': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Level']"}),
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