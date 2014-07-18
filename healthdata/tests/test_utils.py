'''Tests for healthdata/utils.py'''
from django.test import TestCase
from boundaryservice.models import Boundary, BoundarySet
from data.models import Census
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
            B07013_001E=1404,
            B07013_004E=788,
            B08303_001E=941,
            B08303_008E=20,
            B08303_009E=10,
            B08303_010E=13,
            B08303_011E=12,
            B08303_012E=68,
            B08303_013E=0,
            B09002_001E=4.00,
            B09002_008E=0.00,
            B12001_001E=3191,
            B12001_003E=1354,
            B12001_005E=137,
            B12001_009E=19,
            B12001_012E=374,
            B12001_014E=145,
            B12001_018E=66,
            B15002_001E=2616.0,
            B15002_011E=624.0,
            B15002_012E=130.0,
            B15002_013E=254.0,
            B15002_014E=54.0,
            B15002_015E=229.0,
            B15002_016E=64.0,
            B15002_017E=21.0,
            B15002_018E=6.0,
            B15002_028E=179.0,
            B15002_029E=40.0,
            B15002_030E=68.0,
            B15002_031E=41.0,
            B15002_032E=185.0,
            B15002_033E=53.0,
            B15002_034E=13.0,
            B15002_035E=15.0,
            B15003_001E=2616,
            B15003_021E=95,
            B15003_022E=414,
            B15003_023E=117,
            B15003_024E=34,
            B15003_025E=21,
            B17001_001E=1643,
            B17001_002E=534,
            B19058_001E=1042,
            B19058_002E=500,
            B19058_003E=825,
            B23001_001E=3186,
            B23001_008E=0.00,
            B23001_015E=0.00,
            B23001_022E=0.00,
            B23001_029E=0.00,
            B23001_036E=23.0,
            B23001_043E=40.0,
            B23001_050E=23.0,
            B23001_057E=22.0,
            B23001_064E=0.00,
            B23001_071E=0.00,
            B23001_076E=0.00,
            B23001_081E=10.0,
            B23001_086E=0.00,
            B23001_094E=0.00,
            B23001_101E=0.00,
            B23001_108E=0.00,
            B23001_115E=0.00,
            B23001_122E=8.00,
            B23001_129E=5.00,
            B23001_136E=0.00,
            B23001_143E=0.00,
            B23001_150E=0.00,
            B23001_157E=0.00,
            B23001_162E=0.00,
            B23001_167E=0.00,
            B23001_172E=0.00,
            B25014_001E=1042,
            B25014_003E=127,
            B25014_004E=20,
            B25014_005E=0,
            B25014_006E=0,
            B25014_007E=0,
            B25014_009E=645,
            B25014_010E=231,
            B25014_011E=0,
            B25014_012E=19,
            B25014_013E=0,
            B25048_001E=1042,
            B25048_003E=0,
            B25052_001E=1042,
            B25052_003E=7,
            B25070_001E=895.0,
            B25070_008E=52.0,
            B25070_009E=54.0,
            B25070_010E=215.0,
            B25075_001E=147,
            B25075_002E=0,
            B25075_003E=0,
            B25075_004E=0,
            B25075_005E=0,
            B25075_006E=0,
            B25075_007E=0,
            B25075_008E=0,
            B25075_009E=19,
            B25075_010E=4,
            B25075_011E=9,
            B25075_012E=44,
            B25075_013E=6,
            B25075_014E=27,
            B25075_015E=12,
            B25091_001E=147.0,
            B25091_009E=0.00,
            B25091_010E=4.00,
            B25091_011E=11.0,
            B25091_020E=0.00,
            B25091_021E=0.00,
            B25091_022E=0.00,
        )

        Census.objects.create(
            boundary=self.bound_two,
            logical_num=4846,
            B07013_001E=1404,
            B07013_004E=788,
            B08303_001E=941,
            B08303_008E=20,
            B08303_009E=10,
            B08303_010E=13,
            B08303_011E=12,
            B08303_012E=68,
            B08303_013E=0,
            B09002_001E=4.00,
            B09002_008E=0.00,
            B12001_001E=3191,
            B12001_003E=1354,
            B12001_005E=137,
            B12001_009E=19,
            B12001_012E=374,
            B12001_014E=145,
            B12001_018E=66,
            B15002_001E=2616.0,
            B15002_011E=624.0,
            B15002_012E=130.0,
            B15002_013E=254.0,
            B15002_014E=54.0,
            B15002_015E=229.0,
            B15002_016E=64.0,
            B15002_017E=21.0,
            B15002_018E=6.0,
            B15002_028E=179.0,
            B15002_029E=40.0,
            B15002_030E=68.0,
            B15002_031E=41.0,
            B15002_032E=185.0,
            B15002_033E=53.0,
            B15002_034E=13.0,
            B15002_035E=15.0,
            B15003_001E=2616,
            B15003_021E=95,
            B15003_022E=414,
            B15003_023E=117,
            B15003_024E=34,
            B15003_025E=21,
            B17001_001E=1643,
            B17001_002E=534,
            B19058_001E=1042,
            B19058_002E=1000,
            B19058_003E=825,
            B23001_001E=3186,
            B23001_008E=0.00,
            B23001_015E=0.00,
            B23001_022E=0.00,
            B23001_029E=0.00,
            B23001_036E=23.0,
            B23001_043E=40.0,
            B23001_050E=23.0,
            B23001_057E=22.0,
            B23001_064E=0.00,
            B23001_071E=0.00,
            B23001_076E=0.00,
            B23001_081E=10.0,
            B23001_086E=0.00,
            B23001_094E=0.00,
            B23001_101E=0.00,
            B23001_108E=0.00,
            B23001_115E=0.00,
            B23001_122E=8.00,
            B23001_129E=5.00,
            B23001_136E=0.00,
            B23001_143E=0.00,
            B23001_150E=0.00,
            B23001_157E=0.00,
            B23001_162E=0.00,
            B23001_167E=0.00,
            B23001_172E=0.00,
            B25014_001E=1042,
            B25014_003E=127,
            B25014_004E=20,
            B25014_005E=0,
            B25014_006E=0,
            B25014_007E=0,
            B25014_009E=645,
            B25014_010E=231,
            B25014_011E=0,
            B25014_012E=19,
            B25014_013E=0,
            B25048_001E=1042,
            B25048_003E=0,
            B25052_001E=1042,
            B25052_003E=7,
            B25070_001E=895.0,
            B25070_008E=52.0,
            B25070_009E=54.0,
            B25070_010E=215.0,
            B25075_001E=147,
            B25075_002E=0,
            B25075_003E=0,
            B25075_004E=0,
            B25075_005E=0,
            B25075_006E=0,
            B25075_007E=0,
            B25075_008E=0,
            B25075_009E=19,
            B25075_010E=4,
            B25075_011E=9,
            B25075_012E=44,
            B25075_013E=6,
            B25075_014E=27,
            B25075_015E=12,
            B25091_001E=147.0,
            B25091_009E=0.00,
            B25091_010E=4.00,
            B25091_011E=11.0,
            B25091_020E=0.00,
            B25091_021E=0.00,
            B25091_022E=0.00,
        )


class ForAreaState(object):
    def setUp(self):
        Census.objects.create(
            boundary=self.bound_three,
            logical_num=4846,
            B07013_001E=1404,
            B07013_004E=788,
            B08303_001E=941,
            B08303_008E=20,
            B08303_009E=10,
            B08303_010E=13,
            B08303_011E=12,
            B08303_012E=68,
            B08303_013E=0,
            B09002_001E=4.00,
            B09002_008E=0.00,
            B12001_001E=3191,
            B12001_003E=1354,
            B12001_005E=137,
            B12001_009E=19,
            B12001_012E=374,
            B12001_014E=145,
            B12001_018E=66,
            B15002_001E=2616.0,
            B15002_011E=624.0,
            B15002_012E=130.0,
            B15002_013E=254.0,
            B15002_014E=54.0,
            B15002_015E=229.0,
            B15002_016E=64.0,
            B15002_017E=21.0,
            B15002_018E=6.0,
            B15002_028E=179.0,
            B15002_029E=40.0,
            B15002_030E=68.0,
            B15002_031E=41.0,
            B15002_032E=185.0,
            B15002_033E=53.0,
            B15002_034E=13.0,
            B15002_035E=15.0,
            B15003_001E=2616,
            B15003_021E=95,
            B15003_022E=414,
            B15003_023E=117,
            B15003_024E=34,
            B15003_025E=21,
            B17001_001E=1643,
            B17001_002E=534,
            B19058_001E=1042,
            B19058_002E=500,
            B19058_003E=825,
            B23001_001E=3186,
            B23001_008E=0.00,
            B23001_015E=0.00,
            B23001_022E=0.00,
            B23001_029E=0.00,
            B23001_036E=23.0,
            B23001_043E=40.0,
            B23001_050E=23.0,
            B23001_057E=22.0,
            B23001_064E=0.00,
            B23001_071E=0.00,
            B23001_076E=0.00,
            B23001_081E=10.0,
            B23001_086E=0.00,
            B23001_094E=0.00,
            B23001_101E=0.00,
            B23001_108E=0.00,
            B23001_115E=0.00,
            B23001_122E=8.00,
            B23001_129E=5.00,
            B23001_136E=0.00,
            B23001_143E=0.00,
            B23001_150E=0.00,
            B23001_157E=0.00,
            B23001_162E=0.00,
            B23001_167E=0.00,
            B23001_172E=0.00,
            B25014_001E=1042,
            B25014_003E=127,
            B25014_004E=20,
            B25014_005E=0,
            B25014_006E=0,
            B25014_007E=0,
            B25014_009E=645,
            B25014_010E=231,
            B25014_011E=0,
            B25014_012E=19,
            B25014_013E=0,
            B25048_001E=1042,
            B25048_003E=0,
            B25052_001E=1042,
            B25052_003E=7,
            B25070_001E=895.0,
            B25070_008E=52.0,
            B25070_009E=54.0,
            B25070_010E=215.0,
            B25075_001E=147,
            B25075_002E=0,
            B25075_003E=0,
            B25075_004E=0,
            B25075_005E=0,
            B25075_006E=0,
            B25075_007E=0,
            B25075_008E=0,
            B25075_009E=19,
            B25075_010E=4,
            B25075_011E=9,
            B25075_012E=44,
            B25075_013E=6,
            B25075_014E=27,
            B25075_015E=12,
            B25091_001E=147.0,
            B25091_009E=0.00,
            B25091_010E=4.00,
            B25091_011E=11.0,
            B25091_020E=0.00,
            B25091_021E=0.00,
            B25091_022E=0.00,
        )


class GetFieldForAreaTest(ForAreaTestNoData, ForAreaCounty):

    def setUp(self):
        ForAreaTestNoData.setUp(self)
        ForAreaCounty.setUp(self)

    def test_get_field_for_area_intersection(self):
        '''
        Two areas, bound one (500 in field being tested) and bound two(1000 in
        field being tested.) 1/25 of bound one is inside area_to_get_got, and
        of bound two is inside area_to_get_got.  Therefore, the expcted result
         is ((1/25) * 500) + ((9/25) * 1000) = 380
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


class HighestResStateNoTests(ForAreaTestNoData, ForAreaCounty):
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


class HighestResDataStateWith(ForAreaTestNoData, ForAreaState, ForAreaCounty):
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
