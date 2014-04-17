'''Algorithms for calculating scores'''

from collections import OrderedDict
import random

from django.utils.text import slugify


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
