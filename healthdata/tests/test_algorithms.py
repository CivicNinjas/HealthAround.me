import json

from boundaryservice.models import Boundary, BoundarySet
from django.test import TestCase as BaseTestCase

from data.models import Census, Dartmouth, Ers
from healthdata.algorithms import AlgorithmCache
from healthdata.models import ScoreMetric, ScoreNode
from healthdata.utils import fake_boundary


class TestCase(BaseTestCase):
    maxDiff = None

    def assertScoreEqual(self, expected, calculated):
        '''
        Assert calculated is equal to the equivalent dict

        calculated includes OrderDicts, so it is serialized through
        JSON to turn them into plain dicts
        '''
        actual = json.loads(json.dumps(calculated))
        self.assertDictEqual(expected, actual)


class FakeAlgorithmTest(TestCase):
    def setUp(self):
        self.point = (-95.9907, 36.1524)
        self.boundary = fake_boundary(self.point, 2)
        self.cache = AlgorithmCache()

    def assertRandomResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.18,
                u"value": 0.64,
                u"value_type": u"percent",
                u"description": u"A random statistic",
            },
            u"detail": {
                u"path": u"/api/detail/fake_2_-96.00_36.15/random-stat/",
                u"score_text": {
                    u'markdown': (
                        u"We don't have data for Random Stat yet, but studies"
                        u" show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" [Tell us about it](#)."),
                    u'html': (
                        u"<p>We don't have data for Random Stat yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href=\"#\">Tell us about it</a>.</p>"),
                },
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_-96.00_36.15/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def random_stat_node(self):
        metric = ScoreMetric.objects.create(
            name=u"Random Stat",
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM,
            description=u"A random statistic")
        return ScoreNode(
            slug='random-stat', metric=metric, label='Random Stat')

    def test_calculate_random_stat_by_boundary(self):
        node = self.random_stat_node()
        calculated = node.score_by_boundary(self.boundary, self.cache)
        self.assertRandomResult(calculated)

    def test_calculate_random_stat_by_location(self):
        node = self.random_stat_node()
        location = (-95.994, 36.153)
        score = node.score_by_location(location, self.cache)
        self.assertRandomResult(score)

    def test_score_other_random_stat_by_boundary(self):
        metric = ScoreMetric.objects.create(
            name=u"Other Random Stat",
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM,
            description=u"Another random statistic")
        node = ScoreNode(
            slug='other-stat', metric=metric, label='Other Stat')
        score = node.score_by_boundary(self.boundary, self.cache)
        expected = {
            u"summary": {
                u"score": 0.03,
                u"value": 0.76,
                u"value_type": u"percent",
                u"description": u"Another random statistic",
            },
            u"detail": {
                u"path": (
                    u"/api/detail/fake_2_-96.00_36.15/other-stat/"),
                u"score_text": {
                    u'markdown': (
                        u"We don't have data for Other Stat yet, but studies"
                        u" show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" [Tell us about it](#)."),
                    u'html': (
                        u"<p>We don't have data for Other Stat yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href=\"#\">Tell us about it</a>.</p>"),
                },
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_-96.00_36.15/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)


class DartmouthPercentAlgorithmTest(TestCase):
    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='County',
            slug='counties',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
        shape = (
            'MULTIPOLYGON((('
            '-96.03327 35.901100, -96.029570 35.901110, -96.029550 35.901905, '
            '-96.02952 35.993660, -96.029760 35.994770, -96.029500 35.998294, '
            '-96.02982 36.000630, -96.029490 36.017735, -96.029580 36.075370, '
            '-96.15431 36.075770, -96.154840 36.075660, -96.182740 36.075720, '
            '-96.18508 36.075562, -96.190350 36.075545, -96.203730 36.075870, '
            '-96.21060 36.075775, -96.211370 36.075270, -96.211840 36.075179, '
            '-96.21275 36.075260, -96.213810 36.075720, -96.259570 36.075775, '
            '-96.26129 36.075740, -96.261740 36.075570, -96.283600 36.075570, '
            '-96.29779 36.075779, -96.297890 36.090481, -96.297780 36.104281, '
            '-96.29792 36.125090, -96.298090 36.131140, -96.297890 36.162279, '
            '-96.24785 36.161890, -96.176650 36.161130, -96.165780 36.160885, '
            '-96.10878 36.161099, -96.081300 36.160956, -96.074480 36.161189, '
            '-96.07360 36.161031, -96.064430 36.161090, -96.062980 36.160870, '
            '-96.06248 36.161034, -96.057530 36.161090, -96.001050 36.161294, '
            '-96.00147 36.164990, -96.001070 36.166590, -96.001280 36.168487, '
            '-96.00118 36.172992, -96.001380 36.175470, -96.001170 36.180320, '
            '-96.00124 36.188764, -96.001100 36.191482, -96.001380 36.205290, '
            '-96.00128 36.212990, -96.001480 36.219190, -96.001180 36.273890, '
            '-96.00152 36.283065, -96.001430 36.311046, -96.001570 36.319237, '
            '-96.00129 36.343510, -96.001320 36.370202, -96.001190 36.371074, '
            '-96.00118 36.375091, -96.000850 36.375084, -96.001060 36.375479, '
            '-96.00118 36.379027, -96.001310 36.396490, -96.001342 36.412330, '
            '-96.00117 36.423690, -95.866240 36.423752, -95.821180 36.423470, '
            '-95.79437 36.423580, -95.794250 36.394456, -95.812190 36.394340, '
            '-95.81225 36.277797, -95.812060 36.249530, -95.815340 36.249530, '
            '-95.81525 36.235070, -95.815000 36.230600, -95.815000 36.229410, '
            '-95.81524 36.227995, -95.815280 36.224336, -95.814960 36.222300, '
            '-95.81533 36.206133, -95.815400 36.162630, -95.772600 36.162580, '
            '-95.76165 36.162750, -95.761750 36.140706, -95.761650 36.137721, '
            '-95.76181 36.137209, -95.761663 36.133690, -95.761720 36.084741, '
            '-95.76156 36.061723, -95.761650 36.057321, -95.761860 36.055354, '
            '-95.76163 36.051204, -95.761545 35.934090, -95.761550 35.933300, '
            '-95.76185 35.933104, -95.761460 35.920570, -95.761460 35.913800, '
            '-95.76169 35.900811, -95.783330 35.900900, -95.795290 35.901115, '
            '-95.81945 35.901095, -95.819260 35.885173, -95.819350 35.872505, '
            '-95.81940 35.871090, -95.819730 35.871091, -95.819960 35.855900, '
            '-95.86567 35.856100, -95.883970 35.856494, -95.890540 35.856335, '
            '-95.91089 35.856420, -95.917940 35.856710, -95.922240 35.856485, '
            '-95.96109 35.856680, -95.963950 35.856820, -95.979790 35.856882, '
            '-95.98881 35.856740, -95.996100 35.856820, -95.996760 35.857153, '
            '-95.99755 35.856834, -96.015090 35.856930, -96.015870 35.856814, '
            '-96.03312 35.856820, -96.033260 35.872574, -96.033020 35.872830, '
            '-96.03296 35.873261, -96.033093 35.874080, -96.033270 35.885700, '
            '-96.03327 35.901100)))')
        self.county = Boundary.objects.create(
            slug='tulsa-county',
            name='Tulsa County',
            set=self.tract_set,
            metadata={'GEOID': '40143'},
            external_id='40143',
            shape=shape,
            display_name='Tulsa County',
            kind='County',
            simple_shape=shape,
            centroid="POINT (95.941481 36.121077)")
        self.location = (-95.99, 36.15)
        Dartmouth.objects.create(
            boundary=self.county,
            discharge_rate_per_capita=0.2234
        )
        self.cache = AlgorithmCache()

    def discharge_rate_node(self):
        metric = ScoreMetric.objects.create(
            name="Hospital Discharge Rate",
            algorithm=ScoreMetric.PERCENT_DISCHARGE_RATE_ALGORITHM,
            description=(
                "Hospital Discharge Rates per Medicare Enrollee")
        )
        return ScoreNode(slug='discharge-rate', metric=metric)

    def assertDischargeRateResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.792,
                u"value": 0.223,
                u"average": 0.29159,
                u"std_dev": 0.08387,
                u"value_type": u"percent",
                u"description": (
                    u"Hospital Discharge Rates per Medicare Enrollee"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/discharge-rate/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_discharge_rate_by_boundary(self):
        node = self.discharge_rate_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertDischargeRateResults(score)

    def test_discharge_rate_by_location(self):
        node = self.discharge_rate_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertDischargeRateResults(score)


class ErsAlgorithmTest(TestCase):
    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='County',
            slug='counties',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
        shape = (
            'MULTIPOLYGON((('
            '-96.03327 35.901100, -96.029570 35.901110, -96.029550 35.901905, '
            '-96.02952 35.993660, -96.029760 35.994770, -96.029500 35.998294, '
            '-96.02982 36.000630, -96.029490 36.017735, -96.029580 36.075370, '
            '-96.15431 36.075770, -96.154840 36.075660, -96.182740 36.075720, '
            '-96.18508 36.075562, -96.190350 36.075545, -96.203730 36.075870, '
            '-96.21060 36.075775, -96.211370 36.075270, -96.211840 36.075179, '
            '-96.21275 36.075260, -96.213810 36.075720, -96.259570 36.075775, '
            '-96.26129 36.075740, -96.261740 36.075570, -96.283600 36.075570, '
            '-96.29779 36.075779, -96.297890 36.090481, -96.297780 36.104281, '
            '-96.29792 36.125090, -96.298090 36.131140, -96.297890 36.162279, '
            '-96.24785 36.161890, -96.176650 36.161130, -96.165780 36.160885, '
            '-96.10878 36.161099, -96.081300 36.160956, -96.074480 36.161189, '
            '-96.07360 36.161031, -96.064430 36.161090, -96.062980 36.160870, '
            '-96.06248 36.161034, -96.057530 36.161090, -96.001050 36.161294, '
            '-96.00147 36.164990, -96.001070 36.166590, -96.001280 36.168487, '
            '-96.00118 36.172992, -96.001380 36.175470, -96.001170 36.180320, '
            '-96.00124 36.188764, -96.001100 36.191482, -96.001380 36.205290, '
            '-96.00128 36.212990, -96.001480 36.219190, -96.001180 36.273890, '
            '-96.00152 36.283065, -96.001430 36.311046, -96.001570 36.319237, '
            '-96.00129 36.343510, -96.001320 36.370202, -96.001190 36.371074, '
            '-96.00118 36.375091, -96.000850 36.375084, -96.001060 36.375479, '
            '-96.00118 36.379027, -96.001310 36.396490, -96.001342 36.412330, '
            '-96.00117 36.423690, -95.866240 36.423752, -95.821180 36.423470, '
            '-95.79437 36.423580, -95.794250 36.394456, -95.812190 36.394340, '
            '-95.81225 36.277797, -95.812060 36.249530, -95.815340 36.249530, '
            '-95.81525 36.235070, -95.815000 36.230600, -95.815000 36.229410, '
            '-95.81524 36.227995, -95.815280 36.224336, -95.814960 36.222300, '
            '-95.81533 36.206133, -95.815400 36.162630, -95.772600 36.162580, '
            '-95.76165 36.162750, -95.761750 36.140706, -95.761650 36.137721, '
            '-95.76181 36.137209, -95.761663 36.133690, -95.761720 36.084741, '
            '-95.76156 36.061723, -95.761650 36.057321, -95.761860 36.055354, '
            '-95.76163 36.051204, -95.761545 35.934090, -95.761550 35.933300, '
            '-95.76185 35.933104, -95.761460 35.920570, -95.761460 35.913800, '
            '-95.76169 35.900811, -95.783330 35.900900, -95.795290 35.901115, '
            '-95.81945 35.901095, -95.819260 35.885173, -95.819350 35.872505, '
            '-95.81940 35.871090, -95.819730 35.871091, -95.819960 35.855900, '
            '-95.86567 35.856100, -95.883970 35.856494, -95.890540 35.856335, '
            '-95.91089 35.856420, -95.917940 35.856710, -95.922240 35.856485, '
            '-95.96109 35.856680, -95.963950 35.856820, -95.979790 35.856882, '
            '-95.98881 35.856740, -95.996100 35.856820, -95.996760 35.857153, '
            '-95.99755 35.856834, -96.015090 35.856930, -96.015870 35.856814, '
            '-96.03312 35.856820, -96.033260 35.872574, -96.033020 35.872830, '
            '-96.03296 35.873261, -96.033093 35.874080, -96.033270 35.885700, '
            '-96.03327 35.901100)))')
        self.county = Boundary.objects.create(
            slug='tulsa-county',
            name='Tulsa County',
            set=self.tract_set,
            metadata={'GEOID': '40143'},
            external_id='40143',
            shape=shape,
            display_name='Tulsa County',
            kind='County',
            simple_shape=shape,
            centroid="POINT (95.941481 36.121077)")
        self.location = (-95.99, 36.15)
        Ers.objects.create(
            boundary=self.county,
            per_adult_obesity=0.302,
            per_adult_diabetes=0.103,
            rec_facilities_per_capita=0.0001212,
            fast_food_rest_per_capita=0.0008615,
            full_rest_per_capita=0.0007829,
            farmers_markets_per_capita=0.0000163,
            per_low_access_to_groceries=0.255236,
            grocery_stores_per_capita=0.0001327,
            per_students_for_free_lunch=0.481355,
            per_students_for_reduced_lunch=0.084127,
        )
        self.cache = AlgorithmCache()

    def adult_obesity_node(self):
        metric = ScoreMetric.objects.create(
            name="Adult Obesity Rate",
            algorithm=ScoreMetric.PERCENT_ADULT_OBESITY_ALGORITHM,
            description="Percent of Adults that are obese")
        return ScoreNode(slug='adult-obesity', metric=metric)

    def assertAdultObesityRateResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.916,
                u"value": 0.302,
                u"average": 0.33388,
                u"std_dev": 0.02308,
                u"value_type": u"percent",
                u"description": u"Percent of Adults that are obese",
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/adult-obesity/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_adult_obesity_by_boundary(self):
        node = self.adult_obesity_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertAdultObesityRateResults(score)

    def test_adult_obesity_by_location(self):
        node = self.adult_obesity_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertAdultObesityRateResults(score)

    def adult_diabetes_node(self):
        metric = ScoreMetric.objects.create(
            name="Adult Diabetes Rate",
            algorithm=ScoreMetric.PERCENT_ADULT_DIABETES_ALGORITHM,
            description="Percent of Adults that are Diabetic")
        return ScoreNode(slug='adult-diabetes', metric=metric)

    def assertAdultDiabetesRateResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.913,
                u"value": 0.103,
                u"average": 0.1227,
                u"std_dev": 0.01451,
                u"value_type": u"percent",
                u"description": (
                    u"Percent of Adults that are Diabetic"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/adult-diabetes/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_adult_diabetes_by_boundary(self):
        node = self.adult_diabetes_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertAdultDiabetesRateResults(score)

    def test_adult_diabetes_by_location(self):
        node = self.adult_diabetes_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertAdultDiabetesRateResults(score)

    def adult_fitness_center_node(self):
        metric = ScoreMetric.objects.create(
            name="Fitness Centers per Capita",
            algorithm=ScoreMetric.FITNESS_CENTERS_PER_CAPITA_ALGORITHM,
            description="Fitness and Recreation Centers per Capita",
        )
        return ScoreNode(slug='fitness-centers', metric=metric)

    def assertFitnessCentersPerCapitaResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.958,
                u"value": 0.0,
                u"average": 0.0000334103,
                u"std_dev": 0.0000508600,
                u"value_type": u"percent",
                u"description": (
                    u"Fitness and Recreation Centers per Capita"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/fitness-centers/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_adult_fitness_centers_by_boundary(self):
        node = self.adult_fitness_center_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertFitnessCentersPerCapitaResults(score)

    def test_adult_fitness_by_location(self):
        node = self.adult_fitness_center_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertFitnessCentersPerCapitaResults(score)

    def fast_food_node(self):
        metric = ScoreMetric.objects.create(
            name="Fast Food Restaurants per Capita",
            algorithm=ScoreMetric.FAST_FOOD_PER_THOUSAND_ALGORITHM,
            description=(
                "Fast Food Restaurants per Capita")
        )
        return ScoreNode(slug='fast-food', metric=metric)

    def assertFastFoodPerThousandResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.059,
                u"value": 0.001,
                u"average": 0.0004844545,
                u"std_dev": 0.0002416161,
                u"value_type": u"percent",
                u"description": (
                    u"Fast Food Restaurants per Capita"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/fast-food/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_fast_food_by_boundary(self):
        node = self.fast_food_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertFastFoodPerThousandResults(score)

    def test_fast_food_by_location(self):
        node = self.fast_food_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertFastFoodPerThousandResults(score)

    def full_rest_node(self):
        metric = ScoreMetric.objects.create(
            name="Full Service Restaurants per Capita",
            algorithm=ScoreMetric.FULL_REST_PER_THOUSAND_ALGORITHM,
            description=(
                "Full Service Restaurants per Capita")
        )
        return ScoreNode(slug='full-rest', metric=metric)

    def assertFullRestPerThousandResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.274,
                u"value": 0.001,
                u"average": 0.0006372740,
                u"std_dev": 0.0002420894,
                u"value_type": u"percent",
                u"description": (
                    u"Full Service Restaurants per Capita"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/full-rest/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_full_rest_by_boundary(self):
        node = self.full_rest_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertFullRestPerThousandResults(score)

    def test_full_rest_by_location(self):
        node = self.full_rest_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertFullRestPerThousandResults(score)

    def farmers_markets_node(self):
        metric = ScoreMetric.objects.create(
            name="Farmers' Markets per Capita",
            algorithm=ScoreMetric.FARMERS_MARKETS_PER_THOUSAND_ALGORITHM,
            description=(
                "Farmers' Markets per Capita")
        )
        return ScoreNode(slug='farmers-markets', metric=metric)

    def assertFarmersMarketsPerThousandResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.417,
                u"value": 0.0,
                u"average": 0.0000248259,
                u"std_dev": 0.0000409239,
                u"value_type": u"percent",
                u"description": (
                    u"Farmers' Markets per Capita"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/farmers-markets/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_farmers_markets_by_boundary(self):
        node = self.farmers_markets_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertFarmersMarketsPerThousandResults(score)

    def test_farmers_markets_by_location(self):
        node = self.farmers_markets_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertFarmersMarketsPerThousandResults(score)

    def grocery_access_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent with Low Access to Groceries",
            algorithm=ScoreMetric.PERCENT_LOW_ACCESS_TO_GROCERIES_ALGORITHM,
            description=(
                "Percent with Low Access to Groceries")
        )
        return ScoreNode(slug='low-grocery', metric=metric)

    def assertPercentLowAccessToGroceriesResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.549,
                u"value": 0.255,
                u"average": 0.278403948,
                u"std_dev": 0.187626943,
                u"value_type": u"percent",
                u"description": (
                    u"Percent with Low Access to Groceries"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/low-grocery/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_low_groceries_by_boundary(self):
        node = self.grocery_access_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertPercentLowAccessToGroceriesResults(score)

    def test_low_groceries_by_location(self):
        node = self.grocery_access_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentLowAccessToGroceriesResults(score)

    def groceries_per_thousand_node(self):
        metric = ScoreMetric.objects.create(
            name="Grocery Stores per Capita",
            algorithm=ScoreMetric.GROCERY_STORES_PER_THOUSAND_ALGORITHM,
            description=(
                "Grocery Stores per Capita")
        )
        return ScoreNode(slug='groceries-per', metric=metric)

    def assertGroceryStoresPerThousandResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.29,
                u"value": 0.0,
                u"average": 0.0002111467,
                u"std_dev": 0.0001415997,
                u"value_type": u"percent",
                u"description": (
                    u"Grocery Stores per Capita"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/groceries-per/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_groceries_per_thousand_by_boundary(self):
        node = self.groceries_per_thousand_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertGroceryStoresPerThousandResults(score)

    def test_groceries_per_thousand_by_location(self):
        node = self.groceries_per_thousand_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertGroceryStoresPerThousandResults(score)

    def percent_free_lunch_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent of Students Qualifying for a Free Lunch",
            algorithm=ScoreMetric.PERCENT_FREE_LUNCH_ALGORITHM,
            description=(
                "Percent of Students Qualifying for a Free Lunch")
        )
        return ScoreNode(slug='free-lunch', metric=metric)

    def assertPercentFreeLunchResults(self, score):
        expected = {
            u"summary": {
                u"score": 0.715,
                u"value": 0.481,
                u"average": 0.53579519,
                u"std_dev": 0.095828258,
                u"value_type": u"percent",
                u"description": (
                    u"Percent of Students Qualifying for a Free Lunch"),
            },
            u'detail': {
                u"path": u"/api/detail/tulsa-county/free-lunch/",
            },
            u"boundary": {
                u"path": u"/api/boundary/tulsa-county/",
                u"label": u"Tulsa County",
                u"type": u"County",
                u"external_id": u'40143',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_free_lunch_by_boundary(self):
        node = self.percent_free_lunch_node()
        score = node.score_by_boundary(self.county, self.cache)
        self.assertPercentFreeLunchResults(score)

    def test_percent_free_lunch_by_location(self):
        node = self.percent_free_lunch_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentFreeLunchResults(score)


class CensusPercentAlgorithmTest(TestCase):
    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='Census Tract',
            slug='census-tracts',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
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
        self.tract = Boundary.objects.create(
            slug='census-tract-25',
            name='Census Tract 25',
            set=self.tract_set,
            metadata={'GEOID': '40143002500'},
            external_id='40143002500',
            shape=shape,
            display_name='Census Tract 25',
            kind='Census Tract',
            simple_shape=shape,
            centroid="POINT (-95.9907 36.1525)")
        self.location = (-95.99, 36.15)
        Census.objects.create(
            boundary=self.tract,
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
            B19058_002E=217,
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
        self.cache = AlgorithmCache()

    def food_stamp_node(self):
        metric = ScoreMetric.objects.create(
            name="% Food Stamp",
            algorithm=ScoreMetric.FOOD_STAMP_ALGORITHM,
            description=(
                "% of households on public assistance income or food"
                " stamps/SNAP in the past 12 months")
        )
        return ScoreNode(slug='food-stamp', metric=metric)

    def assertFoodStampResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.254,
                u"value": 0.208,
                u"average": 0.138,
                u"std_dev": 0.106,
                u"value_type": u"percent",
                u"description": (
                    u"% of households on public assistance income or food"
                    u" stamps/SNAP in the past 12 months"),
            },
            u'detail': {
                u"path": u"/api/detail/census-tract-25/food-stamp/",
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_food_stamp_by_boundary(self):
        node = self.food_stamp_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertFoodStampResult(score)

    def test_food_stamp_by_location(self):
        node = self.food_stamp_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertFoodStampResult(score)

    def percent_poverty_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Poverty",
            algorithm=ScoreMetric.PERCENT_POVERTY_ALGORITHM,
            description=(
                "Percent Poverty status in the past 12 months")
        )
        return ScoreNode(
            slug='percent-poverty', metric=metric, label='Percent Poverty')

    def assertPercentPovertyResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.09,
                u"value": 0.325,
                u"average": 0.166,
                u"std_dev": 0.118383,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-poverty/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_poverty_by_boundary(self):
        node = self.percent_poverty_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentPovertyResult(score)

    def test_percent_poverty_by_location(self):
        node = self.percent_poverty_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentPovertyResult(score)

    def test_by_location_skips_null_boundary(self):
        block_group_set = BoundarySet.objects.create(
            name='Census Block Groups',
            slug='census-block-groups',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
        shape = (
            'MULTIPOLYGON ((('
            '-96.00269 36.14836, -96.00217 36.14869, -96.00213 36.14798, '
            '-95.99806 36.14791, -95.99935 36.15051, -95.99702 36.15139, '
            '-95.99649 36.15038, -95.98948 36.15279, -95.98841 36.15086, '
            '-95.98952 36.15050, -95.98733 36.14637, -95.98732 36.14377, '
            '-95.99231 36.14423, -95.99455 36.14527, -95.99611 36.14555, '
            '-95.99969 36.14541, -96.00182 36.14595, -96.00260 36.14702, '
            '-96.00269 36.14836)))')
        block_group = Boundary.objects.create(
            slug='census-block-group-002500-1',
            name='002500 1',
            set=block_group_set,
            metadata={'GEOID': '40143002500'},
            external_id='401430025001',
            shape=shape,
            display_name='Census Block Group 002500 1',
            kind='Census Block Group',
            simple_shape=shape)
        Census.objects.create(
            boundary=block_group,
            logical_num=7506,
            B17001_001E=None,
            B17001_002E=None)
        node = self.percent_poverty_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentPovertyResult(score)

    def test_by_boundary_no_data_loads_placeholder(self):
        node = self.percent_poverty_node()
        Census.objects.all().delete()
        score = node.score_by_boundary(self.tract, self.cache)
        expected = {
            u"summary": {
                u"score": 0.31,
                u"value": 0.14,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u"detail": {
                u"path": u"/api/detail/fake_2_-96.00_36.15/percent-poverty/",
                u"score_text": {
                    u'markdown': (
                        u"We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" [Tell us about it](#)."),
                    u'html': (
                        u"<p>We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href=\"#\">Tell us about it</a>.</p>"),
                },
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_-96.00_36.15/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def test_by_location_no_boundary_is_placeholder(self):
        node = self.percent_poverty_node()
        score = node.score_by_location((0, 0), self.cache)
        expected = {
            u"summary": {
                u"score": 0.66,
                u"value": 0.41,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u"detail": {
                u"path": u"/api/detail/fake_2_0.00_0.00/percent-poverty/",
                u"score_text": {
                    u'markdown': (
                        u"We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" [Tell us about it](#)."),
                    u'html': (
                        u"<p>We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href=\"#\">Tell us about it</a>.</p>"),
                },
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_0.00_0.00/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def add_metric_poverty_overrides(self, metric):
        metric.params = {
            'stats': {
                'average': 0.300,
                'std_dev': 0.025,
                'better_sign': 1,
            },
            'score_md_fmt': (
                "In **{boundary}**, **{value}** of people live in a household"
                " where the income is below the poverty level, versus"
                " **{average}** in {domain}.  This puts it in the **{rel}**."),
            'why_md_fmt': (
                "Living below the poverty level is associated with food"
                " insufficiency, transportation problems, and lack of"
                " community support, which leads to poor health in children"
                " and adults, such as increased stomachaches, headaches,"
                " colds, and iron deficiencies."),
            'references': [{
                'link': 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1446676/',
                'title': (
                    'Food insufficiency, family income, and health in US'
                    ' preschool and school-aged children'),
                'publisher': 'NIH',
                'date': 'May 2001',
            }],
            'more_data': [{
                'type': 'census_reporter',
                'table': 'B17001',
                'text': 'View poverty status on CensusReporter.org',
            }],
            'extra_str': 'extra',
            'extra_list': [1, 2, 3],
            'extra_dict': {'foo': 'bar'},
        }
        metric.save()

    def test_metric_overrides(self):
        node = self.percent_poverty_node()
        self.add_metric_poverty_overrides(node.metric)
        score = node.score_by_boundary(self.tract, self.cache)
        expected = {
            u"summary": {
                u"score": 0.841,
                u"value": 0.325,
                u"average": 0.300,
                u"std_dev": 0.025,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-poverty/"),
                u"score_text": {
                    u"markdown": (
                        u"In **Census Tract 25**, **32%** of people live in a"
                        u" household where the income is below the poverty"
                        u" level, versus **30%** in Oklahoma.  This puts it in"
                        u" the **top 16%**."),
                    u"html": (
                        u"<p>In <strong>Census Tract 25</strong>,"
                        u" <strong>32%</strong> of people live in a household"
                        u" where the income is below the poverty level, versus"
                        u" <strong>30%</strong> in Oklahoma.  This puts it in"
                        u" the <strong>top 16%</strong>.</p>"),
                },
                u"why_text": {
                    u"markdown": (
                        u"Living below the poverty level is associated with"
                        u" food insufficiency, transportation problems, and"
                        u" lack of community support, which leads to poor"
                        u" health in children and adults, such as increased"
                        u" stomachaches, headaches, colds, and iron"
                        u" deficiencies."),
                    u"html": (
                        u"<p>Living below the poverty level is associated with"
                        u" food insufficiency, transportation problems, and"
                        u" lack of community support, which leads to poor"
                        u" health in children and adults, such as increased"
                        u" stomachaches, headaches, colds, and iron"
                        u" deficiencies.</p>"),
                },
                u"references": [{
                    u'link': (
                        u'http://www.ncbi.nlm.nih.gov/pmc/articles/'
                        u'PMC1446676/'),
                    u'title': (
                        u'Food insufficiency, family income, and health in'
                        u' US preschool and school-aged children'),
                    u'publisher': u'NIH',
                    u'date': u'May 2001',
                    u'markdown': (
                        u'[Food insufficiency, family income, and health'
                        u' in US preschool and school-aged children]'
                        u'(http://www.ncbi.nlm.nih.gov/pmc/articles/'
                        u'PMC1446676/), NIH, May 2001'),
                    u'html': (
                        u'<p><a href="http://www.ncbi.nlm.nih.gov/pmc/'
                        u'articles/PMC1446676/">Food insufficiency,'
                        u' family income, and health in US preschool and'
                        u' school-aged children</a>, NIH, May 2001</p>'),
                }],
                u"more_data": [{
                    u'type': u'census_reporter',
                    u'table': u'B17001',
                    u'text': u'View poverty status on CensusReporter.org',
                    u'link': (
                        u'http://censusreporter.org/data/table/?table=B17001'
                        u'&geo_ids=14000US40143002500'
                        u'&primary_geo_id=14000US40143002500'),
                    u'markdown': (
                        u'[View poverty status on CensusReporter.org]'
                        u'(http://censusreporter.org/data/table/?table=B17001'
                        u'&geo_ids=14000US40143002500'
                        u'&primary_geo_id=14000US40143002500)'),
                    u'html': (
                        u'<p><a href="http://censusreporter.org/data/table/'
                        u'?table=B17001'
                        u'&amp;geo_ids=14000US40143002500'
                        u'&amp;primary_geo_id=14000US40143002500">'
                        u'View poverty status on CensusReporter.org</a></p>'),
                }],
                u'extra_str': u'extra',
                u'extra_list': [1, 2, 3],
                u'extra_dict': {u'foo': u'bar'},
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_metric_overrides_with_placeholder(self):
        node = self.percent_poverty_node()
        self.add_metric_poverty_overrides(node.metric)
        score = node.score_by_location((0, 0), self.cache)
        expected = {
            u"summary": {
                u"score": 0.66,
                u"value": 0.41,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/fake_2_0.00_0.00/percent-poverty/"),
                u"score_text": {
                    u"markdown": (
                        u"We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" [Tell us about it](#)."),
                    u"html": (
                        u"<p>We don't have data for Percent Poverty yet, but"
                        u" studies show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href=\"#\">Tell us about it</a>.</p>"),
                },
                u"why_text": {
                    u"markdown": (
                        u"Living below the poverty level is associated with"
                        u" food insufficiency, transportation problems, and"
                        u" lack of community support, which leads to poor"
                        u" health in children and adults, such as increased"
                        u" stomachaches, headaches, colds, and iron"
                        u" deficiencies."),
                    u"html": (
                        u"<p>Living below the poverty level is associated with"
                        u" food insufficiency, transportation problems, and"
                        u" lack of community support, which leads to poor"
                        u" health in children and adults, such as increased"
                        u" stomachaches, headaches, colds, and iron"
                        u" deficiencies.</p>"),
                },
                u"references": [{
                    u'link': (
                        u'http://www.ncbi.nlm.nih.gov/pmc/articles/'
                        u'PMC1446676/'),
                    u'title': (
                        u'Food insufficiency, family income, and health in'
                        u' US preschool and school-aged children'),
                    u'publisher': u'NIH',
                    u'date': u'May 2001',
                    u'markdown': (
                        u'[Food insufficiency, family income, and health'
                        u' in US preschool and school-aged children]'
                        u'(http://www.ncbi.nlm.nih.gov/pmc/articles/'
                        u'PMC1446676/), NIH, May 2001'),
                    u'html': (
                        u'<p><a href="http://www.ncbi.nlm.nih.gov/pmc/'
                        u'articles/PMC1446676/">Food insufficiency,'
                        u' family income, and health in US preschool and'
                        u' school-aged children</a>, NIH, May 2001</p>'),
                }],
                u"more_data": [{
                    u'type': u'census_reporter',
                    u'table': u'B17001',
                    u'text': u'View poverty status on CensusReporter.org',
                    u'link': (
                        u'http://censusreporter.org/data/table/?table=B17001'
                        u'&geo_ids=04000US40'
                        u'&primary_geo_id=04000US40'),
                    u'markdown': (
                        u'[View poverty status on CensusReporter.org]'
                        u'(http://censusreporter.org/data/table/?table=B17001'
                        u'&geo_ids=04000US40'
                        u'&primary_geo_id=04000US40)'),
                    u'html': (
                        u'<p><a href="http://censusreporter.org/data/table/'
                        u'?table=B17001'
                        u'&amp;geo_ids=04000US40'
                        u'&amp;primary_geo_id=04000US40">'
                        u'View poverty status on CensusReporter.org</a></p>'),
                }],
                u'extra_str': u'extra',
                u'extra_list': [1, 2, 3],
                u'extra_dict': {u'foo': u'bar'},
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_0.00_0.00/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def test_metric_empty_overrides(self):
        node = self.percent_poverty_node()
        node.metric.params = {}
        node.metric.save()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentPovertyResult(score)

    def percent_employment_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Unemployment",
            algorithm=ScoreMetric.PERCENT_UNEMPLOYMENT_ALGORITHM,
            description="Percent Unemployment in the past 12 months",
        )
        return ScoreNode(slug='percent-employment', metric=metric)

    def assertPercentEmploymentResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.512,
                u"value": 0.041,
                u"average": 0.04193,
                u"std_dev": 0.0266,
                u"value_type": "percent",
                u"description": "Percent Unemployment in the past 12 months",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-employment/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_employment_by_boundary(self):
        node = self.percent_employment_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentEmploymentResult(score)

    def test_percent_employment_by_location(self):
        node = self.percent_employment_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentEmploymentResult(score)

    def percent_single_parent_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Single Parent",
            algorithm=ScoreMetric.PERCENT_SINGLE_PARENT_ALGORITHM,
            description="Percent of Children Living with a Single Parent",
        )
        return ScoreNode(slug='percent-single-parent', metric=metric)

    def assertPercentSingleParentResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.997,
                u"value": 0.0,
                u"average": 0.452998,
                u"std_dev": 0.1657150,
                u"value_type": u"percent",
                u"description": (
                    u"Percent of Children Living with a Single Parent")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-single-parent/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_single_parent_by_boundary(self):
        node = self.percent_single_parent_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentSingleParentResult(score)

    def test_percent_single_parent_by_location(self):
        node = self.percent_single_parent_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentSingleParentResult(score)

    def percent_income_housing_cost_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Income Housing Cost",
            algorithm=ScoreMetric.PERCENT_INCOME_HOUSING_COST_ALGORITHM,
            description=(
                "Data calculated from values in both of these tables."),
        )
        return ScoreNode(
            slug='percent-income-housing-cost-node', metric=metric)

    def assertPercentIncomeHousingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.118,
                u"value": 0.257,
                u"average": 0.1544959,
                u"std_dev": 0.0867039,
                u"value_type": u"percent",
                u"description": (
                    u"Data calculated from values in both of these tables."),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-income-housing-cost-node/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_income_housing_cost_by_boundary(self):
        node = self.percent_income_housing_cost_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentIncomeHousingResult(score)

    def test_percent_income_housing_cost_by_location(self):
        node = self.percent_income_housing_cost_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentIncomeHousingResult(score)

    def percent_high_school_graduates_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent High School Graduates",
            algorithm=ScoreMetric.PERCENT_HIGH_SCHOOL_GRADUATES_ALGORITHM,
            description=(
                "Educational Attainment for the Population 25 Years and Over")
        )
        return ScoreNode(
            slug='percent-high-school-graduates', metric=metric)

    def assertPercentHighSchoolGraduatesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.136,
                u"value": 0.755,
                u"average": 0.861836,
                u"std_dev": 0.096739,
                u"value_type": u"percent",
                u"description": (
                    u"Educational Attainment for the Population"
                    u" 25 Years and Over"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-high-school-graduates/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_high_school_graduates_by_boundary(self):
        node = self.percent_high_school_graduates_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentHighSchoolGraduatesResult(score)

    def test_percent_high_school_graduates_by_location(self):
        node = self.percent_high_school_graduates_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentHighSchoolGraduatesResult(score)

    def percent_divorced_or_separated_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Divorced or Separated",
            algorithm=ScoreMetric.PERCENT_DIVORCED_ALGORITHM,
            description=(
                "Percent of Population Divorced or Separated"
                " 15 Years and Over")
        )
        return ScoreNode(slug='percent-divorced-married', metric=metric)

    def assertPercentDivorcedOrSeparatedResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.0,
                u"value": 0.795,
                u"average": 0.264508,
                u"std_dev": 0.139789,
                u"value_type": u"percent",
                u"description": (
                    "Percent of Population Divorced or Separated"
                    " 15 Years and Over")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-divorced-married/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_divorced_or_separated_by_boundary(self):
        node = self.percent_divorced_or_separated_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentDivorcedOrSeparatedResult(score)

    def test_percent_divorced_or_separated_by_location(self):
        node = self.percent_divorced_or_separated_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentDivorcedOrSeparatedResult(score)

    def percent_overcrowded_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Overcrowding in Residences",
            algorithm=ScoreMetric.PERCENT_OVERCROWDING_ALGORITHM,
            description="Tenure by Occupants per Room",
        )
        return ScoreNode(slug='percent-overcrowded', metric=metric)

    def assertPercentOvercrowdedResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.536,
                u"value": 0.039,
                u"average": 0.040577,
                u"std_dev": 0.014887,
                u"value_type": u"percent",
                u"description": "Tenure by Occupants per Room",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-overcrowded/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_overcrowded_by_boundary(self):
        node = self.percent_overcrowded_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentOvercrowdedResult(score)

    def test_percent_overcrowded_by_location(self):
        node = self.percent_overcrowded_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentOvercrowdedResult(score)

    def percent_geographic_mobility_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Geographic Movement in a Year",
            algorithm=ScoreMetric.PERCENT_GEOGRAPHIC_MOBILITY_ALGORITHM,
            description=(
                "Geographic Mobility in the Past Year by Tenure for Current"
                " Residence in the United States")
        )
        return ScoreNode(slug='percent-geographic-mobility', metric=metric)

    def assertPercentGeographicMobilityResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.002,
                u"value": 0.439,
                u"average": 0.168965,
                u"std_dev": 0.09219,
                u"value_type": u"percent",
                u"description": (
                    "Geographic Mobility in the Past Year by Tenure for"
                    " Current Residence in the United States"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-geographic-mobility/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_geographic_mobility_by_boundary(self):
        node = self.percent_geographic_mobility_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentGeographicMobilityResult(score)

    def test_percent_geographic_mobility_by_location(self):
        node = self.percent_geographic_mobility_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentGeographicMobilityResult(score)

    def percent_college_graduates_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent College Graduates",
            algorithm=ScoreMetric.PERCENT_COLLEGE_GRADUATE_ALGORITHM,
            description=(
                "Educational Attainment for the Population 25 Years and Over")
        )
        return ScoreNode(slug='percent-college-graduate', metric=metric)

    def assertPercentCollegeGraduateResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.394,
                u"value": 0.26,
                u"average": 0.301417,
                u"std_dev": 0.153007,
                u"value_type": u"percent",
                u"description": (
                    u"Educational Attainment for the Population"
                    u" 25 Years and Over")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-college-graduate/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_college_graduate_by_boundary(self):
        node = self.percent_college_graduates_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentCollegeGraduateResult(score)

    def test_percent_college_graduate_by_location(self):
        node = self.percent_college_graduates_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentCollegeGraduateResult(score)

    def percent_bad_commute_times_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Bad Commute Times",
            algorithm=ScoreMetric.PERCENT_BAD_COMMUTE_TIMES_ALGORITHM,
            description="Travel Time to Work",
        )
        return ScoreNode(slug='percent-bad-commute-times', metric=metric)

    def assertPercentBadCommuteTimesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.488,
                u"value": 0.085,
                u"average": 0.082964,
                u"std_dev": 0.059340889,
                u"value_type": u"percent",
                u"description": u"Travel Time to Work",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-bad-commute-times/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_bad_commute_times_by_boundary(self):
        node = self.percent_bad_commute_times_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentBadCommuteTimesResult(score)

    def test_percent_bad_commute_times_by_location(self):
        node = self.percent_bad_commute_times_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentBadCommuteTimesResult(score)

    def percent_improper_kitchen_facilities_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Improper Kitchen Facilities",
            algorithm=(
                ScoreMetric.PERCENT_IMPROPER_KITCHEN_FACILITIES_ALGORITHM),
            description="Kitchen Facilities for Occupied Housing Units",
        )
        return ScoreNode(
            slug='percent-improper-kitchen-facilities', metric=metric)

    def assertPercentImproperKitchenFacilitiesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.567,
                u"value": 0.007,
                u"average": 0.00976313,
                u"std_dev": 0.01802429,
                u"value_type": u"percent",
                u"description": (
                    u"Kitchen Facilities for Occupied Housing Units"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25"
                    u"/percent-improper-kitchen-facilities/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_improper_kitchen_facilities_by_boundary(self):
        node = self.percent_improper_kitchen_facilities_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentImproperKitchenFacilitiesResult(score)

    def test_percent_improper_kitchen_facilities_by_location(self):
        node = self.percent_improper_kitchen_facilities_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentImproperKitchenFacilitiesResult(score)

    def percent_improper_plumbing_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Improper Plumbing",
            algorithm=ScoreMetric.PERCENT_IMPROPER_PLUMBING_ALGORITHM,
            description="Plumbing Facilities for Occupied Housing Units",
        )
        return ScoreNode(slug='percent-improper-plumbing', metric=metric)

    def assertPercentImproperPlumbingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.7,
                u"value": 0.0,
                u"average": 0.00572503,
                u"std_dev": 0.0109313,
                u"value_type": u"percent",
                u"description": (
                    u"Plumbing Facilities for Occupied Housing Units"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-improper-plumbing/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_improper_plumbing_by_boundary(self):
        node = self.percent_improper_plumbing_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentImproperPlumbingResult(score)

    def test_percent_improper_plumbing_by_location(self):
        node = self.percent_improper_plumbing_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentImproperPlumbingResult(score)

    def percent_low_value_housing_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Low Value Housing",
            algorithm=ScoreMetric.PERCENT_LOW_VALUE_HOUSING_ALGORITHM,
            description="Value",
        )
        return ScoreNode(slug='percent-low-value-housing', metric=metric)

    def assertPercentLowValueHousingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.755,
                u"value": 0.018,
                u"average": 0.0575880,
                u"std_dev": 0.057490381,
                u"value_type": u"percent",
                u"description": u"Value",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-low-value-housing/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_low_value_housing_by_boundary(self):
        node = self.percent_low_value_housing_node()
        score = node.score_by_boundary(self.tract, self.cache)
        self.assertPercentLowValueHousingResult(score)

    def test_percent_low_value_housing_by_location(self):
        node = self.percent_low_value_housing_node()
        score = node.score_by_location(self.location, self.cache)
        self.assertPercentLowValueHousingResult(score)
