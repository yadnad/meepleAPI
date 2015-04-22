from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from apps.api.views import (artist, category, designer, expansion, family, game, mechanic,
                            publisher, subdomain, resource)


urlpatterns = [
    url(r'^games/', include(game, namespace='game')),
    url(r'^expansions/', include(expansion, namespace='expansion')),
    url(r'^artists/', include(artist, namespace='artist')),
    url(r'^designers/', include(designer, namespace='designer')),
    url(r'^publishers/', include(publisher, namespace='publisher')),
    url(r'^mechanics/', include(mechanic, namespace='mechanic')),
    url(r'^subdomains/', include(subdomain, namespace='subdomain')),
    url(r'^categories/', include(category, namespace='category')),
    url(r'^families/', include(family, namespace='family')),
    url(r'^$', include(resource, namespace='root')),
]

urlpatterns = format_suffix_patterns(urlpatterns)