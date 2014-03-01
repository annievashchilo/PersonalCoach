# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrainingType'
        db.create_table(u'trainings_trainingtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('load', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('trainings', ['TrainingType'])


    def backwards(self, orm):
        # Deleting model 'TrainingType'
        db.delete_table(u'trainings_trainingtype')


    models = {
        'trainings.trainingtype': {
            'Meta': {'object_name': 'TrainingType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'load': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['trainings']