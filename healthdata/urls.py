from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from .views import (
    BoundaryAPIView, DetailAPIView, FakeBoundaryAPIView, FeedbackView,
    ScoreAPIView)

api_urls = patterns(
    '',
    url(r'^score-fake/.*$', 'healthdata.views.fake_api'),
    url(r'^score-old/(?P<lon>-?[\d.]+),(?P<lat>-?[\d.]+)/$',
        'healthdata.views.score_by_location'),
    url(r'^score/(?P<lon>-?[\d.]+),(?P<lat>-?[\d.]+)/$',
        ScoreAPIView.as_view(), name='score'),
    url(r'^boundary/(?P<slug>fake_[-_\d.]*)/$',
        FakeBoundaryAPIView.as_view(), name='fake-boundary'),
    url(r'^boundary/(?P<slug>[a-z\-_\d]*)/$', BoundaryAPIView.as_view(),
        name='boundary'),
    url(r'^detail/(?P<boundary_slug>[a-z\-_\d.]*)'
        r'/(?P<node_slug>[a-z\-_\d]*)/$',
        DetailAPIView.as_view(), name='metric-detail'),
    url(r'feedback/$', FeedbackView.as_view(), name='feedback')
)

urlpatterns = patterns(
    'healthdata.views',
    url(r'^$', TemplateView.as_view(template_name='healthdata/home.jinja2'),
        name='home'),
    url(r'^tryit/$',
        TemplateView.as_view(template_name='healthdata/try_it.jinja2'),
        name='try_it'),
    url(r'^api/', include(api_urls, 'api')),
)
