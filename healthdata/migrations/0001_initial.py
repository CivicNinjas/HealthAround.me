# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProtoHealth'
        db.create_table(u'healthdata_protohealth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boundary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['boundaryservice.Boundary'], null=True, blank=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('deaths', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perc_poor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_lbw', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_smokers', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_obese', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('std_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('teen_birth_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mammography_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_unemployed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_children_poverty', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('violent_crime', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ozone_days', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perc_limited_food', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perc_fast_food', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'healthdata', ['ProtoHealth'])


    def backwards(self, orm):
        # Deleting model 'ProtoHealth'
        db.delete_table(u'healthdata_protohealth')


    models = {
        u'boundaryservice.boundary': {
            'Meta': {'ordering': "('kind', 'display_name')", 'object_name': 'Boundary'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '4269', 'null': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'metadata': ('boundaryservice.fields.JSONField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '192', 'db_index': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boundaries'", 'to': u"orm['boundaryservice.BoundarySet']"}),
            'shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'simple_shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'boundaryservice.boundaryset': {
            'Meta': {'ordering': "('name',)", 'object_name': 'BoundarySet'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_first': ('django.db.models.fields.BooleanField', [], {}),
            'last_updated': ('django.db.models.fields.DateField', [], {}),
            'metadata_fields': ('boundaryservice.fields.ListField', [], {'separator': "'|'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'singular': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'healthdata.protohealth': {
            'Meta': {'object_name': 'ProtoHealth'},
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boundaryservice.Boundary']", 'null': 'True', 'blank': 'True'}),
            'deaths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mammography_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ozone_days': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perc_children_poverty': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_fast_food': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_lbw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_limited_food': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_obese': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_poor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_smokers': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perc_unemployed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'std_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'teen_birth_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'violent_crime': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['healthdata']
