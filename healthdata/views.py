import json
import os.path

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

def fake_api(request):
    path = os.path.join(settings.BASE_DIR, 'TestData', 'SampleData.json')
    content = json.load(file(path, 'r'))
    response = HttpResponse(json.dumps(content, indent=2))
    response['Content-Type'] = 'application/json'
    return response
