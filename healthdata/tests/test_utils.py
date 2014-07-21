'''Tests for healthdata/utils.py'''
from django.test import TestCase
from boundaryservice.models import Boundary, BoundarySet
from data.models import Census, Dartmouth
from django.contrib.gis.geos import GEOSGeometry

from healthdata.utils import (
    fake_boundary,
    get_field_for_area,
    highest_resolution_for_data
)


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


class ForAreaTestNoData(TestCase):
    def setUp(self):
        self.county_set = BoundarySet.objects.create(
            name='County',
            slug='counties',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])

        bound_one_shape = GEOSGeometry(
            'MULTIPOLYGON((('
            '-95.5 36.0, -95.5 36.5, -95.0 36.5,'
            '-95.0 36.0, -95.5 36.0)))'
        )

        bound_two_shape = GEOSGeometry(
            'MULTIPOLYGON((('
            '-95.5 36.0, -95.5 36.5, -96.0 36.5,'
            '-96.0 36.0, -95.5 36.0)))'
        )

        self.bound_one = Boundary.objects.create(
            slug='county-one',
            name='County One',
            set=self.county_set,
            metadata={'GEOID': '40143'},
            external_id='40143',
            shape=bound_one_shape,
            display_name='County One',
            kind='County',
            simple_shape=bound_one_shape,
            centroid="POINT (-95.25 36.25)")

        self.bound_two = Boundary.objects.create(
            slug='county-two',
            name='County Two',
            set=self.county_set,
            metadata={'GEOID': '40109'},
            external_id='40109',
            shape=bound_two_shape,
            display_name='County Two',
            kind='County',
            simple_shape=bound_two_shape,
            centroid="POINT (-95.75 36.25)")

        self.state_set = BoundarySet.objects.create(
            name='State',
            slug='states',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])

        bound_three_shape = GEOSGeometry(
            'MUlTIPOLYGON((('
            '-97.0 35.5, -97.0 37.0, -94.0 37.0,'
            '-94.0 35.5, -97.0 35.5)))'
        )

        self.bound_three = Boundary.objects.create(
            slug='state-one',
            name='State One',
            set=self.state_set,
            metadata={'GEOID': '40100'},
            external_id='40100',
            shape=bound_three_shape,
            display_name='State One',
            kind='State',
            simple_shape=bound_three_shape,
            centroid="POINT (-95.5 36.25)"
        )


class ForAreaCounty(object):
    def setUp(self):

        Census.objects.create(
            boundary=self.bound_one,
            logical_num=4846,
            B01003_001E=1500,
            B19058_002E=500,
        )

        Census.objects.create(
            boundary=self.bound_two,
            logical_num=4846,
            B01003_001E=2500,
            B19058_002E=1000,
        )


class ForAreaState(object):
    def setUp(self):
        Census.objects.create(
            boundary=self.bound_three,
            logical_num=4846,
            B19058_002E=500,
        )


class ForAreaCountyPer(object):
    def setUp(self):
        Dartmouth.objects.create(
            boundary=self.bound_one,
            discharge_rate_per_capita=0.25
        )

        Dartmouth.objects.create(
            boundary=self.bound_one,
            discharge_rate_per_capita=0.5
        )


class FieldForAreaTest(ForAreaTestNoData, ForAreaCounty):

    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaCounty.setUp(self)

    def test_get_field_for_area_intersection(self):
        '''
        Two areas, bound one (500 in field being tested) and bound two(1000 in
        field being tested.) 1/25 of bound one is inside area_to_get_got, and
        9/25ths of bound two is inside area_to_get_got. Therefore, the expcted
        result is ((1/25) * 500) + ((9/25) * 1000) = 380
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.95 36.15, -95.45 36.15,'
            '-95.45 36.35,-95.95 36.35, -95.95 36.15)))')
        self.assertEqual(get_field_for_area(
            area_to_get_got,
            'B19058_002E',
            Census
        ), 380)

    def test_get_field_for_area_inside(self):
        '''
        In this test, area_to_get_got is completely inside bound two and
        is equal to 1/25 of bound two's area. Bound two has a population
        of 1000 in the field we are getting. Therefore, the expected
        result is equal to (1/25)* 1000 = 40
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.9 36.15, -95.8 36.15,'
            '-95.8 36.25, -95.9 36.25, -95.9 36.15)))')
        self.assertEqual(
            get_field_for_area(
                area_to_get_got,
                'B19058_002E',
                Census
            ), 40)

    def test_get_field_for_area_partially_outside_data(self):
        '''
        In this test, 2/3 of area_to_get_got is inside bound two, taking
        up 2/25ths of bound two's total area, while the last 1/3 of
        area_to_get_got is outside of it.  The algorithm will ignore this
        overlap in to areas that don't contain any of the data we're looking
        for, so we need only concern ourselves with the area inside bound two.
        Expected Result: (2/25) * 1000 = 80
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-96.1 36.15, -95.8 36.15,'
            '-95.8 36.25, -96.1 36.25, -96.1 36.15)))')
        self.assertEqual(
            get_field_for_area(
                area_to_get_got,
                'B19058_002E',
                Census
            ), 80)

    def test_get_field_for_area_outside_data(self):
        '''
        In this test, area_to_get is defined as being somewhere in the arctic.
        The get_field_for_area should return a string indicating that there is
        no data in that area.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-51.0 81.0, -52.0 81.0,'
            '-52.0 82.0, -51.0 82.0, -51.0 81.0)))'
        )
        self.assertEqual(
            get_field_for_area(
                area_to_get_got,
                'B19058_002E',
                Census
            ), "No data for that field in given area."
        )


class FieldForAreaPerTest(ForAreaTestNoData, ForAreaCounty, ForAreaCountyPer):
    '''
    Two areas, bound one(0.25 per capita discharge rate) and bound two(0.5 per
    capita discharge rate.)  1/25 o
    '''
    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaCounty.setUp(self)
        ForAreaCountyPer.setUp(self)


class HighestResStateNo(ForAreaTestNoData):
    def setUp(self):
        ForAreaTestNoData.setUp(self)

    def test_state_and_county_no_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside both
        a county and a state, where a census table containing the data we are
        looking for is paired with neither the county nor the state. Should
        return None.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.32 36.4, -95.31 36.4,'
            '-95.31 36.45, -95.32 36.45, -95.32 36.4)))'
        )
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), None
        )


class HighestResStateNoTest(ForAreaTestNoData, ForAreaCounty):
    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaCounty.setUp(self)

    def test_state_and_county_no_state_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside both
        a county and a state, where a census table containing the data we are
        looking for is paired with the county but not the state. Should
        return county.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.32 36.4, -95.31 36.4,'
            '-95.31 36.45, -95.32 36.45, -95.32 36.4)))'
        )
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), "County"
        )

    def test_state_no_state_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside a
        state and no other boundaries, where the data we are looking for
        is not paired with the state's boundary.  Should return None.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.45 36.8, -95.5 36.8,'
            '-95.5 36.9, -95.45 36.9, -95.45 36.8)))'
        )
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), None
        )


class HighestResCountyNoTest(ForAreaTestNoData, ForAreaState):
    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaState.setUp(self)

    def test_state_and_county_no_county_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside both
        a county and a state, where a census table containing the data we are
        looking for is paired with the state but not the county. Should
        return state.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.32 36.4, -95.31 36.4,'
            '-95.31 36.45, -95.32 36.45, -95.32 36.4)))'
        )
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), "State"
        )

    def test_state_state_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside a
        state and no other boundaries, where the data we are looking for
        is paired with the state's boundary.  Should return State.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.45 36.8, -95.5 36.8,'
            '-95.5 36.9, -95.45 36.9, -95.45 36.8)))'
        )
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), "State"
        )


class HighestResTest(ForAreaTestNoData, ForAreaState, ForAreaCounty):
    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaState.setUp(self)
        ForAreaCounty.setUp(self)

    def test_state_and_county_both_data(self):
        '''
        In this test, area_to_get_got is defined as being located inside both
        a county and a state, where a census table containing the data we are
        looking for is paired with the county and the state. Should
        return county.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-95.32 36.4, -95.31 36.4,'
            '-95.31 36.45, -95.32 36.45, -95.32 36.4)))')
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), "County"
        )

    def test_outside_state_and_county(self):
        '''
        In this test, area_to_get_got is defined as being located outside both
        a county and a state, where a census table containing the data we are
        looking for is paired with the county and the state. Should
        return None.
        '''
        area_to_get_got = GEOSGeometry(
            'MUlTIPOLYGON(((-35.32 36.4, -35.31 36.4,'
            '-35.31 36.45, -35.32 36.45, -35.32 36.4)))')
        self.assertEqual(
            highest_resolution_for_data(
                area_to_get_got,
                'B19058_002E',
                Census
            ), None
        )
