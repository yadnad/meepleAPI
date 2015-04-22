from urlparse import urljoin

from django.conf import settings
from django.conf.urls import url
from django.core.urlresolvers import reverse

from rest_framework.response import Response
from rest_framework.views import APIView
from apps.utils.analytics import keen_hit


class RootView(APIView):

    def dispatch(self, request, *args, **kwargs):
        keen_hit('root', 'root', request)
        return super(RootView, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        """
        Return a list of resources
        """
        links = {
            'games': urljoin(settings.BASE_API, reverse('api-v1:game:game-list')),
            'expansions': urljoin(settings.BASE_API, reverse('api-v1:expansion:expansion-list')),
            'artists': urljoin(settings.BASE_API, reverse('api-v1:artist:artist-list')),
            'designers': urljoin(settings.BASE_API, reverse('api-v1:designer:designer-list')),
            'publishers': urljoin(settings.BASE_API, reverse('api-v1:publisher:publisher-list')),
            'mechanics': urljoin(settings.BASE_API, reverse('api-v1:mechanic:mechanic-list')),
            'subdomains': urljoin(settings.BASE_API, reverse('api-v1:subdomain:subdomain-list')),
            'categories': urljoin(settings.BASE_API, reverse('api-v1:category:category-list')),
            'families': urljoin(settings.BASE_API, reverse('api-v1:family:family-list')),
        }
        return Response(links)


urlpatterns = [
    url(r'^$', RootView.as_view(), name='root'),
]
