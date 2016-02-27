# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LastRequest'
        db.create_table(u'requests_lastrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'requests', ['LastRequest'])


    def backwards(self, orm):
        # Deleting model 'LastRequest'
        db.delete_table(u'requests_lastrequest')


    models = {
        u'requests.lastrequest': {
            'Meta': {'object_name': 'LastRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['requests']