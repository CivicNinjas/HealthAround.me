'''Algorithms for calculating scores'''

from collections import OrderedDict
import random
from django.utils.text import slugify
from scipy.stats import norm

from boundaryservice.models import Boundary
from data.models import Census


def boundaries(point):
    '''Return boundaries containing the point'''
    wkt = 'POINT({} {})'.format(*point)
    return Boundary.objects.filter(shape__contains=wkt)


def boundary_dict(boundary):
    '''Convert a boundary to a dictionary'''
    return OrderedDict((
        ('path', '/api/boundary/{}/'.format(boundary.slug)),
        ('label', boundary.display_name),
        ('year', 2013),
        ('type', boundary.set.name),
        ('external_id', boundary.external_id),
        ('id', boundary.slug),
    ))


class BaseAlgorithm(object):
    def __init__(self, metric):
        self.metric = metric

    def calculate(self, point):
        raise NotImplementedError('Algorithm is not implemented')


class FakeAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        lon, lat = point
        coord_fmt = '{:0.4f}'
        lon_st = coord_fmt.format(lon)
        lat_st = coord_fmt.format(lat)
        slug = slugify(self.metric.name)
        path = "fake/{}/{},{}".format(slug, lon_st, lat_st)
        random.seed(path)
        score = random.randint(0, 100) / 100.0
        value = random.randint(0, 10000) / 100.0
        citation = OrderedDict((
            ('path', '/api/citation/' + path),
            ('label', 'Fake Data Citation'),
            ('year', 2010),
            ('type', 'fake'),
            ('id', '{},{}'.format(lon_st, lat_st)),
        ))
        boundary = OrderedDict((
            ('path', '/api/boundary/' + path),
            ('label', 'Fake Data Boundary'),
            ('year', 2010),
            ('type', 'fake'),
            ('id', '{},{}'.format(lon_st, lat_st)),
        ))
        score = OrderedDict((
            ("score", score),
            ("value", value),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class FoodStampAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B19058_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B19058/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B19058'),
        ))
        total = data.B19058_001E
        on_stamps = data.B19058_002E
        percent = on_stamps / float(total)
        state_avg = 0.138
        state_std_dev = 0.106
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary



class PercentPovertyAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B17001_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B17001/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B17001'),
        ))
        total = data.B17001_001E
        in_poverty = data.B17001_002E
        percent = in_poverty / float(total)
        state_avg = 0.166
        state_std_dev = 0.118383
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary



class PercentUnemploymentAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = (
                    'B23001_001E', 'B23001_008E', 'B23001_015E',
                    'B23001_022E', 'B23001_029E', 'B23001_036E',
                    'B23001_043E', 'B23001_050E', 'B23001_057E',
                    'B23001_064E', 'B23001_071E', 'B23001_076E',
                    'B23001_081E', 'B23001_086E', 'B23001_094E',
                    'B23001_101E', 'B23001_108E', 'B23001_115E',
                    'B23001_122E', 'B23001_129E', 'B23001_136E',
                    'B23001_143E', 'B23001_150E', 'B23001_157E',
                    'B23001_162E', 'B23001_167E', 'B23001_172E',
    )
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B23001_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(*list_of_rows).exclude(B23001_001E=0).first()
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B23001/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B23001'),
        ))
        

        data_list = list(new_data)
        total = data_list.pop(0)
        total_unemployed = sum(data_list)
        percent = total_unemployed / float(total)
        state_avg = 0.04193
        state_std_dev = 0.0266
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary



class PercentIncomeHousingCost(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = (
            'B25106_001E','B25106_006E','B25106_010E',
            'B25106_014E','B25106_018E','B25106_022E',
            'B25106_023E','B25106_028E','B25106_032E',
            'B25106_036E','B25106_040E','B25106_044E',
            'B25106_045E',
        )
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).values_list(*list_of_rows).exclude(
                    B25106_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B23001/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B25106'),
        ))
        
        total = data.pop(0)
        total_unemployed = sum(data)
        percent = total_unemployed / float(total)
        state_avg = 0.166
        state_std_dev = 0.11
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary

class PercentSingleParentChildren(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = (
            'B11003_003E', 'B11003_010E', 'B11003_016E',
        )
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).values_list(*list_of_rows).exclude(
                    B11003_003E=0, B11003_010E=0, B11003_016E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B11003/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B11003'),
        ))
        
        total = sum(data)
        total_single_parent = data.B11003_010E + data.B11003_016E
        percent = total_single_parent / float(total)
        state_avg = 0.332
        state_std_dev = 0.11
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary