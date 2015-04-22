# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.api import urls as api_urls
from apps.web.views import AboutView, DonateView, HomeView, DocsView

from django.contrib import admin

def handler404(request):
    response = render_to_response('404.jinja', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.jinja', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^buy-me-a-coffee/$', DonateView.as_view(), name='donate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^v1/", include(api_urls, namespace='api-v1')),
    url(r"^docs/", DocsView.as_view(), name='docs'),
]
