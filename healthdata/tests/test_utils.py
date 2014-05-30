'''Tests for healthdata/utils.py'''

from boundaryservice.models import Boundary, BoundarySet
from django.test import TestCase

from healthdata.utils import fake_boundary, boundaries_for_location


class FakeBoundaryUtilTest(TestCase):
    def setUp(self):
        self.location = (-95.9910, 36.1499)

    def test_fake_2(self):
        boundary = fake_boundary(self.location, 2)
        self.assertEqual('fake', boundary.name)
        self.assertEqual('Pending Data', boundary.display_name)
        self.assertEqual('Pending Data', boundary.kind)
        self.assertFalse(boundary.external_id)
        self.assertFalse(boundary.id)
        self.assertEqual('fake_2_-96.00_36.14', boundary.slug)
        expected_shape = (((
            (-96., 36.14), (-96., 36.15), (-95.99, 36.15), (-95.99, 36.14),
            (-96., 36.14)),),)
        self.assertEqual(expected_shape, boundary.shape.coords)
        self.assertEqual((-95.995, 36.145), boundary.centroid.coords)

    def test_fake_3(self):
        boundary = fake_boundary(self.location, 3)
        self.assertEqual('fake', boundary.name)
        self.assertEqual('Pending Data', boundary.display_name)
        self.assertEqual('Pending Data', boundary.kind)
        self.assertFalse(boundary.external_id)
        self.assertFalse(boundary.id)
        self.assertEqual('fake_3_-95.991_36.149', boundary.slug)
        expected_shape = (((
            (-95.991, 36.149), (-95.991, 36.15), (-95.99, 36.15),
            (-95.99, 36.149), (-95.991, 36.149)),),)
        self.assertEqual(expected_shape, boundary.shape.coords)
        self.assertEqual((-95.9905, 36.1495), boundary.centroid.coords)


class BoundariesForLocation(TestCase):
    def setUp(self):
        self.location = (-95.9910, 36.1499)
        self.tract_set = BoundarySet.objects.create(
            name='Census Tract',
            slug='census-tracts',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])

    def test_fake(self):
        boundaries = list(boundaries_for_location(self.location, ['fake_3']))
        self.assertEqual(1, len(boundaries))
        boundary = boundaries[0]
        self.assertEqual('fake_3_-95.991_36.149', boundary.slug)

    def test_real(self):
        shape = (
            'MULTIPOLYGON ((('
            '-96.00269 36.14836, -96.00269 36.15019, -96.00154 36.15488, '
            '-96.00169 36.15608, -96.00138 36.15608, -96.00149 36.15648, '
            '-96.00091 36.15798, -96.00060 36.15807, -95.99898 36.16035, '
            '-95.99903 36.16052, -95.99776 36.16078, -95.99788 36.16099, '
            '-95.99532 36.16147, -95.99286 36.16221, -95.99030 36.16237, '
            '-95.98693 36.16103, -95.98393 36.16057, -95.98096 36.15979, '
            '-95.98068 36.15918, -95.98038 36.15274, -95.98059 36.14949, '
            '-95.97970 36.14593, -95.98005 36.14427, -95.98061 36.14340, '
            '-95.98136 36.14282, -95.98243 36.14243, -95.98381 36.14245, '
            '-95.98732 36.14377, -95.99231 36.14423, -95.99455 36.14526, '
            '-95.99611 36.14555, -95.99969 36.14541, -96.00045 36.14555, '
            '-96.00182 36.14595, -96.00224 36.14639, -96.00260 36.14702, '
            '-96.00269 36.14836)))')
        tract = Boundary.objects.create(
            slug='census-tract-25',
            set=self.tract_set,
            metadata={'GEOID': '40143002500'},
            external_id='40143002500',
            shape=shape,
            display_name='Census Tract 25',
            simple_shape=shape)
        boundaries = list(
            boundaries_for_location(self.location, ['census-tracts']))
        self.assertEqual(1, len(boundaries))
        boundary = boundaries[0]
        self.assertEqual(boundary, tract)

    def test_bad_set_slug_raises(self):
        gen = boundaries_for_location(self.location, ['bad-slug'])
        self.assertRaises(BoundarySet.DoesNotExist, list, gen)

    def test_no_boundaries_found(self):
        boundaries = list(
            boundaries_for_location(self.location, ['census-tracts']))
        self.assertFalse(boundaries)
