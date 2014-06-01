'''Tests for healthdata/utils.py'''

from django.test import TestCase

from healthdata.utils import fake_boundary


class FakeBoundaryUtilTest(TestCase):
    def setUp(self):
        self.location = (-95.9910, 36.1499)

    def test_fake_2(self):
        boundary = fake_boundary(self.location, 2)
        self.assertEqual('Placeholder', boundary.name)
        self.assertEqual('Future Data Placeholder', boundary.display_name)
        self.assertEqual('Future Data Placeholder', boundary.kind)
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
        self.assertEqual('Placeholder', boundary.name)
        self.assertEqual('Future Data Placeholder', boundary.display_name)
        self.assertEqual('Future Data Placeholder', boundary.kind)
        self.assertFalse(boundary.external_id)
        self.assertFalse(boundary.id)
        self.assertEqual('fake_3_-95.991_36.149', boundary.slug)
        expected_shape = (((
            (-95.991, 36.149), (-95.991, 36.15), (-95.99, 36.15),
            (-95.99, 36.149), (-95.991, 36.149)),),)
        self.assertEqual(expected_shape, boundary.shape.coords)
        self.assertEqual((-95.9905, 36.1495), boundary.centroid.coords)
