# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Census.B07013_001E'
        db.add_column(u'data_census', 'B07013_001E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_002E'
        db.add_column(u'data_census', 'B07013_002E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_003E'
        db.add_column(u'data_census', 'B07013_003E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_004E'
        db.add_column(u'data_census', 'B07013_004E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_005E'
        db.add_column(u'data_census', 'B07013_005E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_006E'
        db.add_column(u'data_census', 'B07013_006E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_007E'
        db.add_column(u'data_census', 'B07013_007E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_008E'
        db.add_column(u'data_census', 'B07013_008E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_009E'
        db.add_column(u'data_census', 'B07013_009E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_010E'
        db.add_column(u'data_census', 'B07013_010E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_011E'
        db.add_column(u'data_census', 'B07013_011E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_012E'
        db.add_column(u'data_census', 'B07013_012E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_013E'
        db.add_column(u'data_census', 'B07013_013E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_014E'
        db.add_column(u'data_census', 'B07013_014E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_015E'
        db.add_column(u'data_census', 'B07013_015E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_016E'
        db.add_column(u'data_census', 'B07013_016E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_017E'
        db.add_column(u'data_census', 'B07013_017E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B07013_018E'
        db.add_column(u'data_census', 'B07013_018E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_001E'
        db.add_column(u'data_census', 'B15002_001E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_002E'
        db.add_column(u'data_census', 'B15002_002E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_003E'
        db.add_column(u'data_census', 'B15002_003E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_004E'
        db.add_column(u'data_census', 'B15002_004E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_005E'
        db.add_column(u'data_census', 'B15002_005E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_006E'
        db.add_column(u'data_census', 'B15002_006E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_007E'
        db.add_column(u'data_census', 'B15002_007E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_008E'
        db.add_column(u'data_census', 'B15002_008E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_009E'
        db.add_column(u'data_census', 'B15002_009E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_010E'
        db.add_column(u'data_census', 'B15002_010E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_011E'
        db.add_column(u'data_census', 'B15002_011E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_012E'
        db.add_column(u'data_census', 'B15002_012E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_013E'
        db.add_column(u'data_census', 'B15002_013E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_014E'
        db.add_column(u'data_census', 'B15002_014E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_015E'
        db.add_column(u'data_census', 'B15002_015E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_016E'
        db.add_column(u'data_census', 'B15002_016E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_017E'
        db.add_column(u'data_census', 'B15002_017E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_018E'
        db.add_column(u'data_census', 'B15002_018E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_019E'
        db.add_column(u'data_census', 'B15002_019E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_020E'
        db.add_column(u'data_census', 'B15002_020E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_021E'
        db.add_column(u'data_census', 'B15002_021E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_022E'
        db.add_column(u'data_census', 'B15002_022E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_023E'
        db.add_column(u'data_census', 'B15002_023E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_024E'
        db.add_column(u'data_census', 'B15002_024E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_025E'
        db.add_column(u'data_census', 'B15002_025E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_026E'
        db.add_column(u'data_census', 'B15002_026E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_027E'
        db.add_column(u'data_census', 'B15002_027E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_028E'
        db.add_column(u'data_census', 'B15002_028E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_029E'
        db.add_column(u'data_census', 'B15002_029E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_030E'
        db.add_column(u'data_census', 'B15002_030E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_031E'
        db.add_column(u'data_census', 'B15002_031E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_032E'
        db.add_column(u'data_census', 'B15002_032E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_033E'
        db.add_column(u'data_census', 'B15002_033E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_034E'
        db.add_column(u'data_census', 'B15002_034E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B15002_035E'
        db.add_column(u'data_census', 'B15002_035E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_001E'
        db.add_column(u'data_census', 'B25014_001E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_002E'
        db.add_column(u'data_census', 'B25014_002E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_003E'
        db.add_column(u'data_census', 'B25014_003E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_004E'
        db.add_column(u'data_census', 'B25014_004E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_005E'
        db.add_column(u'data_census', 'B25014_005E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_006E'
        db.add_column(u'data_census', 'B25014_006E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_007E'
        db.add_column(u'data_census', 'B25014_007E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_008E'
        db.add_column(u'data_census', 'B25014_008E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_009E'
        db.add_column(u'data_census', 'B25014_009E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_010E'
        db.add_column(u'data_census', 'B25014_010E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_011E'
        db.add_column(u'data_census', 'B25014_011E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_012E'
        db.add_column(u'data_census', 'B25014_012E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25014_013E'
        db.add_column(u'data_census', 'B25014_013E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25048_001E'
        db.add_column(u'data_census', 'B25048_001E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25048_002E'
        db.add_column(u'data_census', 'B25048_002E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Census.B25048_003E'
        db.add_column(u'data_census', 'B25048_003E',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Census.B07013_001E'
        db.delete_column(u'data_census', 'B07013_001E')

        # Deleting field 'Census.B07013_002E'
        db.delete_column(u'data_census', 'B07013_002E')

        # Deleting field 'Census.B07013_003E'
        db.delete_column(u'data_census', 'B07013_003E')

        # Deleting field 'Census.B07013_004E'
        db.delete_column(u'data_census', 'B07013_004E')

        # Deleting field 'Census.B07013_005E'
        db.delete_column(u'data_census', 'B07013_005E')

        # Deleting field 'Census.B07013_006E'
        db.delete_column(u'data_census', 'B07013_006E')

        # Deleting field 'Census.B07013_007E'
        db.delete_column(u'data_census', 'B07013_007E')

        # Deleting field 'Census.B07013_008E'
        db.delete_column(u'data_census', 'B07013_008E')

        # Deleting field 'Census.B07013_009E'
        db.delete_column(u'data_census', 'B07013_009E')

        # Deleting field 'Census.B07013_010E'
        db.delete_column(u'data_census', 'B07013_010E')

        # Deleting field 'Census.B07013_011E'
        db.delete_column(u'data_census', 'B07013_011E')

        # Deleting field 'Census.B07013_012E'
        db.delete_column(u'data_census', 'B07013_012E')

        # Deleting field 'Census.B07013_013E'
        db.delete_column(u'data_census', 'B07013_013E')

        # Deleting field 'Census.B07013_014E'
        db.delete_column(u'data_census', 'B07013_014E')

        # Deleting field 'Census.B07013_015E'
        db.delete_column(u'data_census', 'B07013_015E')

        # Deleting field 'Census.B07013_016E'
        db.delete_column(u'data_census', 'B07013_016E')

        # Deleting field 'Census.B07013_017E'
        db.delete_column(u'data_census', 'B07013_017E')

        # Deleting field 'Census.B07013_018E'
        db.delete_column(u'data_census', 'B07013_018E')

        # Deleting field 'Census.B15002_001E'
        db.delete_column(u'data_census', 'B15002_001E')

        # Deleting field 'Census.B15002_002E'
        db.delete_column(u'data_census', 'B15002_002E')

        # Deleting field 'Census.B15002_003E'
        db.delete_column(u'data_census', 'B15002_003E')

        # Deleting field 'Census.B15002_004E'
        db.delete_column(u'data_census', 'B15002_004E')

        # Deleting field 'Census.B15002_005E'
        db.delete_column(u'data_census', 'B15002_005E')

        # Deleting field 'Census.B15002_006E'
        db.delete_column(u'data_census', 'B15002_006E')

        # Deleting field 'Census.B15002_007E'
        db.delete_column(u'data_census', 'B15002_007E')

        # Deleting field 'Census.B15002_008E'
        db.delete_column(u'data_census', 'B15002_008E')

        # Deleting field 'Census.B15002_009E'
        db.delete_column(u'data_census', 'B15002_009E')

        # Deleting field 'Census.B15002_010E'
        db.delete_column(u'data_census', 'B15002_010E')

        # Deleting field 'Census.B15002_011E'
        db.delete_column(u'data_census', 'B15002_011E')

        # Deleting field 'Census.B15002_012E'
        db.delete_column(u'data_census', 'B15002_012E')

        # Deleting field 'Census.B15002_013E'
        db.delete_column(u'data_census', 'B15002_013E')

        # Deleting field 'Census.B15002_014E'
        db.delete_column(u'data_census', 'B15002_014E')

        # Deleting field 'Census.B15002_015E'
        db.delete_column(u'data_census', 'B15002_015E')

        # Deleting field 'Census.B15002_016E'
        db.delete_column(u'data_census', 'B15002_016E')

        # Deleting field 'Census.B15002_017E'
        db.delete_column(u'data_census', 'B15002_017E')

        # Deleting field 'Census.B15002_018E'
        db.delete_column(u'data_census', 'B15002_018E')

        # Deleting field 'Census.B15002_019E'
        db.delete_column(u'data_census', 'B15002_019E')

        # Deleting field 'Census.B15002_020E'
        db.delete_column(u'data_census', 'B15002_020E')

        # Deleting field 'Census.B15002_021E'
        db.delete_column(u'data_census', 'B15002_021E')

        # Deleting field 'Census.B15002_022E'
        db.delete_column(u'data_census', 'B15002_022E')

        # Deleting field 'Census.B15002_023E'
        db.delete_column(u'data_census', 'B15002_023E')

        # Deleting field 'Census.B15002_024E'
        db.delete_column(u'data_census', 'B15002_024E')

        # Deleting field 'Census.B15002_025E'
        db.delete_column(u'data_census', 'B15002_025E')

        # Deleting field 'Census.B15002_026E'
        db.delete_column(u'data_census', 'B15002_026E')

        # Deleting field 'Census.B15002_027E'
        db.delete_column(u'data_census', 'B15002_027E')

        # Deleting field 'Census.B15002_028E'
        db.delete_column(u'data_census', 'B15002_028E')

        # Deleting field 'Census.B15002_029E'
        db.delete_column(u'data_census', 'B15002_029E')

        # Deleting field 'Census.B15002_030E'
        db.delete_column(u'data_census', 'B15002_030E')

        # Deleting field 'Census.B15002_031E'
        db.delete_column(u'data_census', 'B15002_031E')

        # Deleting field 'Census.B15002_032E'
        db.delete_column(u'data_census', 'B15002_032E')

        # Deleting field 'Census.B15002_033E'
        db.delete_column(u'data_census', 'B15002_033E')

        # Deleting field 'Census.B15002_034E'
        db.delete_column(u'data_census', 'B15002_034E')

        # Deleting field 'Census.B15002_035E'
        db.delete_column(u'data_census', 'B15002_035E')

        # Deleting field 'Census.B25014_001E'
        db.delete_column(u'data_census', 'B25014_001E')

        # Deleting field 'Census.B25014_002E'
        db.delete_column(u'data_census', 'B25014_002E')

        # Deleting field 'Census.B25014_003E'
        db.delete_column(u'data_census', 'B25014_003E')

        # Deleting field 'Census.B25014_004E'
        db.delete_column(u'data_census', 'B25014_004E')

        # Deleting field 'Census.B25014_005E'
        db.delete_column(u'data_census', 'B25014_005E')

        # Deleting field 'Census.B25014_006E'
        db.delete_column(u'data_census', 'B25014_006E')

        # Deleting field 'Census.B25014_007E'
        db.delete_column(u'data_census', 'B25014_007E')

        # Deleting field 'Census.B25014_008E'
        db.delete_column(u'data_census', 'B25014_008E')

        # Deleting field 'Census.B25014_009E'
        db.delete_column(u'data_census', 'B25014_009E')

        # Deleting field 'Census.B25014_010E'
        db.delete_column(u'data_census', 'B25014_010E')

        # Deleting field 'Census.B25014_011E'
        db.delete_column(u'data_census', 'B25014_011E')

        # Deleting field 'Census.B25014_012E'
        db.delete_column(u'data_census', 'B25014_012E')

        # Deleting field 'Census.B25014_013E'
        db.delete_column(u'data_census', 'B25014_013E')

        # Deleting field 'Census.B25048_001E'
        db.delete_column(u'data_census', 'B25048_001E')

        # Deleting field 'Census.B25048_002E'
        db.delete_column(u'data_census', 'B25048_002E')

        # Deleting field 'Census.B25048_003E'
        db.delete_column(u'data_census', 'B25048_003E')


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
        u'data.census': {
            'B01001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B01002_001E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B01002_002E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B01002_003E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B01003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B02001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07013_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B07413_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08006_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08016_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08018_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08301_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B08303_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B09002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B10002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B10002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B10002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B10002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B10002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11003_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B11004_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B12503_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B13004_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14002_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14004_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B14007_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15002_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B15003_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_058E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17001_059E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17003_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B17010_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18101_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B18135_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19013_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19055_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19055_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19055_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19056_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19056_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19056_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19057_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19057_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19057_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19058_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19083_001E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B19113_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B19301_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22002_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B22003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_058E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_059E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_060E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_061E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_062E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_063E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_064E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_065E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_066E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_067E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_068E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_069E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_070E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_071E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_072E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_073E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_074E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_075E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_076E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_077E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_078E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_079E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_080E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_081E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_082E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_083E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_084E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_085E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_086E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_087E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_088E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_089E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_090E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_091E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_092E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_093E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_094E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_095E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_096E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_097E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_098E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_099E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_100E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_101E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_102E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_103E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_104E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_105E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_106E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_107E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_108E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_109E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_110E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_111E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_112E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_113E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_114E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_115E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_116E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_117E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_118E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_119E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_120E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_121E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_122E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_123E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_124E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_125E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_126E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_127E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_128E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_129E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_130E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_131E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_132E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_133E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_134E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_135E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_136E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_137E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_138E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_139E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_140E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_141E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_142E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_143E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_144E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_145E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_146E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_147E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_148E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_149E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_150E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_151E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_152E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_153E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_154E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_155E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_156E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_157E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_158E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_159E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_160E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_161E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_162E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_163E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_164E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_165E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_166E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_167E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_168E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_169E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_170E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_171E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_172E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23001_173E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23020_001E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B23020_002E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B23020_003E': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'B23025_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B23025_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25004_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25014_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25016_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25027_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25034_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25035_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25042_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25048_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25052_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25058_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25064_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25070_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25075_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25087_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25091_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B25106_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27001_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27002_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_022E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_023E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_024E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_025E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_026E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_027E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_028E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_029E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_030E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_031E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_032E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_033E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_034E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_035E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_036E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_037E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_038E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_039E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_040E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_041E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_042E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_043E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_044E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_045E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_046E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_047E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_048E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_049E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_050E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_051E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_052E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_053E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_054E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_055E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_056E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B27003_057E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C17002_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27006_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_001E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_002E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_003E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_004E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_005E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_006E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_007E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_008E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_009E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_010E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_011E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_012E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_013E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_014E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_015E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_016E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_017E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_018E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_019E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_020E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C27007_021E': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Census'},
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['boundaryservice.Boundary']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logical_num': ('django.db.models.fields.IntegerField', [], {}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['data']
