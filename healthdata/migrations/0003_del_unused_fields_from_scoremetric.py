# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ScoreMetric.data_property'
        db.delete_column(u'healthdata_scoremetric', 'data_property')

        # Deleting field 'ScoreMetric.data_source'
        db.delete_column(u'healthdata_scoremetric', 'data_source_id')

        # Deleting field 'ScoreMetric.boundary_set'
        db.delete_column(u'healthdata_scoremetric', 'boundary_set_id')


    def backwards(self, orm):
        # Adding field 'ScoreMetric.data_property'
        db.add_column(u'healthdata_scoremetric', 'data_property',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoreMetric.data_source'
        db.add_column(u'healthdata_scoremetric', 'data_source',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoreMetric.boundary_set'
        db.add_column(u'healthdata_scoremetric', 'boundary_set',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['boundaryservice.BoundarySet'], null=True, blank=True),
                      keep_default=False)


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
        },
        u'healthdata.scoremetric': {
            'Meta': {'object_name': 'ScoreMetric'},
            'algorithm': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'This is a description'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'params': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'healthdata.scorenode': {
            'Meta': {'object_name': 'ScoreNode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'metric': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['healthdata.ScoreMetric']", 'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['healthdata.ScoreNode']"}),
            'rel_order': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['healthdata']