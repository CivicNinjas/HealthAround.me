from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('healthdata.views',
    url(r'^$', TemplateView.as_view(template_name='healthdata/home.jinja2'),
        name='home')
)
