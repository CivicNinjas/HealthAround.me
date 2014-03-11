from collections import OrderedDict
from math import floor
import json
import os.path

from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings
from django.shortcuts import render

from healthdata.models import ScoreNode

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
        scores['score'] = floor(1000.0 *score) / 1000.0
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
        ('scores', scores),
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
