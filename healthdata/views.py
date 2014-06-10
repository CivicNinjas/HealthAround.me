from collections import OrderedDict
from math import floor
import json
import os.path

from boundaryservice.models import Boundary
from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from .algorithms import AlgorithmCache
from .models import Feedback, ScoreNode
from .serializers import (
    BoundarySerializer, MetricDetailSerializer, ScoreNodeSerializer)
from .utils import fake_boundary


def fake_api(request):
    '''Return hand-written JSON'''
    path = os.path.join(settings.BASE_DIR, 'TestData', 'SampleData.json')
    content = json.load(file(path, 'r'))
    callback = request.GET.get('callback')
    if callback:
        out = '{}({});'.format(callback, json.dumps(content))
        response = HttpResponse(out)
        response['Content-Type'] = 'application/javascript'
    else:
        response = HttpResponse(json.dumps(content, indent=2))
        response['Content-Type'] = 'application/json'
    return response


def score_node(node, point):
    '''Recursively generate score nodes, citations, and boundaries

    Return is a 3-element tuple:
    scores - A recursive dictionary of score data
    citations - A dictionary of citation names -> citation data
    boundaries - A dictionary of boundary names -> boundary data
    '''
    citations = {}
    boundaries = {}
    scores = OrderedDict((
        ('label', node.label),
        ('slug', node.slug),
        ('weight', node.weight),
    ))
    if node.metric:
        assert node.is_leaf_node()
        algorithm = node.metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        assert 'score' in score
        assert score['citation_path'] == citation['path']
        assert score['boundary_path'] == boundary['path']
        scores.update(score)
        citations[citation['path']] = citation
        boundaries[boundary['path']] = boundary
    else:
        assert not node.is_leaf_node()
        scores['score'] = 0
        scores['elements'] = []
        child_citations = {}
        child_boundaries = {}
        total_child_weight = 0.0
        for child_node in node.get_children():
            score, citation, boundary = score_node(child_node, point)
            scores['elements'].append(score)
            child_citations.update(citation)
            child_boundaries.update(boundary)
            total_child_weight += child_node.weight
        score = 0.0
        for child_score in scores['elements']:
            cscore = child_score['score']
            cweight = child_score['weight']
            score += (cscore * cweight) / total_child_weight
        scores['score'] = floor(1000.0 * score) / 1000.0
        citations.update(child_citations)
        boundaries.update(child_boundaries)
    return scores, citations, boundaries


def score_by_location(request, lon, lat):
    '''Return score + citation JSON for a lon/lat point

    Return JSON has three top level elements:
    scores - Recursive score tree
    location - Request location and related boundaries
    citations - Data sources used in scoring
    '''
    fmt = request.GET.get('format', 'json')
    callback = request.GET.get('callback')
    point = (float(lon), float(lat))
    if fmt not in ('json',):
        raise HttpResponseBadRequest('{} is not a valid format'.format(fmt))

    scores = []
    citations = {}
    boundaries = {}
    location = OrderedDict((
        ('longitude', point[0]),
        ('latitude', point[1]),
        ('wkt', 'POINT({} {})'.format(*point)),
    ))

    for node in ScoreNode.objects.root_nodes():
        score, citation, boundary = score_node(node, point)
        scores.append(score)
        citations.update(citation)
        boundaries.update(boundary)

    location['boundaries'] = boundaries
    content = OrderedDict((
        ('elements', scores),
        ('location', location),
        ('citations', citations)
    ))

    if callback:
        out = '{}({});'.format(callback, json.dumps(content))
        response = HttpResponse(out)
        response['Content-Type'] = 'application/javascript'
    else:
        response = HttpResponse(json.dumps(content, indent=2))
        response['Content-Type'] = 'application/json'
    return response


class BoundaryAPIView(RetrieveAPIView):
    model = Boundary
    serializer_class = BoundarySerializer


def fake_boundary_from_slug(fake_slug):
    '''Create a fake Boundary from a path slug'''
    _, raw_res, raw_lon, raw_lat = fake_slug.split('_', 4)
    location = (float(raw_lon), float(raw_lat))
    precision = int(raw_res)
    return fake_boundary(location, precision)


class DetailAPIView(RetrieveAPIView):
    model = Boundary
    serializer_class = MetricDetailSerializer

    def transform_data(self, raw_data):
        '''Transform the raw MetricDetailSerializer data'''
        data = raw_data.copy()
        elem = data['properties'].pop('element')

        # Element should be a leaf node
        children = elem.pop('children')
        assert not children

        # Extract summary and detail items
        metric = elem.pop('metric')
        for key, val in metric['summary'].items():
            elem[key] = val
        for key, val in metric['detail'].items():
            if key != 'path':
                elem[key] = val

        data['properties']['metric'] = elem
        return data

    def get_object(self, queryset=None):
        '''Get the boundary, generating a fake boundary as needed'''
        boundary_slug = self.kwargs['boundary_slug']
        if boundary_slug.startswith('fake_'):
            boundary = fake_boundary_from_slug(boundary_slug)
        else:
            boundary = Boundary.objects.get(slug=boundary_slug)
        return boundary

    def get_serializer_context(self):
        '''Add the node to the context'''
        context = super(DetailAPIView, self).get_serializer_context()
        node_slug = self.kwargs['node_slug']
        node = ScoreNode.objects.filter(slug=node_slug).latest('id')
        context['node'] = node
        context['cache'] = AlgorithmCache()
        return context

    def retrieve(self, request, *args, **kwargs):
        '''
        Convert raw node serialization to wire serialization

        Copy of rest_framework/mixins/RetrieveModelMixin.retrieve,
        but transforms the raw MetricDetailSerializer data.
        '''
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        raw_data = serializer.data
        data = self.transform_data(raw_data)
        return Response(data)


class FakeBoundaryAPIView(RetrieveAPIView):
    model = Boundary
    serializer_class = BoundarySerializer

    def get_object(self, queryset=None):
        return fake_boundary_from_slug(self.kwargs['slug'])


class FeedbackView(CreateAPIView):
    model = Feedback

    def get(self, request, *args, **kwargs):
        return Response({})


class ScoreAPIView(ListAPIView):
    serializer_class = ScoreNodeSerializer
    queryset = ScoreNode.objects.filter(parent=None)

    def get_serializer_context(self):
        context = super(ScoreAPIView, self).get_serializer_context()
        context['location'] = (
            float(self.kwargs['lon']),
            float(self.kwargs['lat']))
        context['cache'] = AlgorithmCache()
        return context

    def transform_data(self, raw_data):
        '''Transform the raw ScoreNodeSerializer data'''
        data = OrderedDict((
            ('score', 0),
            ('elements', []),
            ('boundaries', {}),
        ))
        for raw in raw_data:
            transformed = self.transform_raw_element(raw)
            element, boundaries, citations = transformed
            data['elements'].append(element)
            data['boundaries'].update(boundaries)

        # Accumulate score
        total_score = 0.0
        total_weight = 0.0
        for element in data['elements']:
            total_score += element['score'] * element['weight']
            total_weight += element['weight']
        data['score'] = round(total_score / total_weight, 2)

        return data

    def transform_raw_element(self, raw):
        '''Recursively transform a raw element'''
        element = OrderedDict((
            ('label', raw['label']),
            ('slug', raw['slug']),
            ('weight', raw['weight']),
        ))
        boundaries = {}
        citations = {}
        assert raw['metric'] or raw['children']
        if raw['metric']:
            assert not raw['children']
            metric = raw['metric']
            for key, value in metric['summary'].items():
                element[key] = value

            # Extract boundary
            boundary = metric['boundary']
            boundary_path = boundary['path']
            boundary['uri'] = (
                self.request.build_absolute_uri(boundary_path))
            boundary_path_prefix = '/api/boundary/'
            assert boundary_path.startswith(boundary_path_prefix)
            assert boundary_path.endswith('/')
            boundary_id = boundary_path[len(boundary_path_prefix):-1]
            boundaries[boundary_id] = boundary
            element['boundary_id'] = boundary_id

            # Extract detail URI
            detail_path = metric['detail']['path']
            element['detail_uri'] = (
                self.request.build_absolute_uri(detail_path))
        if raw['children']:
            assert not raw['metric']
            total_score = 0.0
            total_weight = 0.0
            child_elements = []
            for child in raw['children']:
                transformed = self.transform_raw_element(child)
                sub_element, sub_boundaries, sub_citations = transformed

                # Add elements and accumulate score
                child_elements.append(sub_element)
                total_score += sub_element['score'] * sub_element['weight']
                total_weight += sub_element['weight']

                # Merge boundaries
                for boundary_path, boundary in sub_boundaries.items():
                    boundaries[boundary_path] = boundary

                # Merge citations
                for citation_path, citation in sub_citations.items():
                    citations[citation_path] = citation
            element['elements'] = child_elements
            element['score'] = round(total_score / total_weight, 2)
        return element, boundaries, citations

    def list(self, request, *args, **kwargs):
        '''
        Convert raw node serialization to wire serialization

        Simplier version of rest_framework/mixins/ListModelMixin.list,
        but transforms the raw ScoreNodeSerializer data.
        '''
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        raw_data = serializer.data
        data = self.transform_data(raw_data)
        return Response(data)
