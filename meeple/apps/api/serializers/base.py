from __future__ import unicode_literals
from urlparse import urljoin

from django.conf import settings
from django.core.urlresolvers import reverse

from rest_framework import serializers

LIST_FIELDS = ('name', 'resource_url')
DETAIL_FIELDS = ('name', 'slug', 'resource_url', 'games', 'expansions')


class BasePropertiesListSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    resource = None

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:{0}:{0}-detail'.format(self.resource),
                                                  args=[obj.id]))


class BasePropertiesDetailSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    games = serializers.SerializerMethodField()
    expansions = serializers.SerializerMethodField()
    resource = None

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:{0}:{0}-detail'.format(self.resource),
                                                  args=[obj.id]))

    def get_games(self, obj):
        count = obj.games.count()
        resource_url = urljoin(settings.BASE_API,
                               reverse('api-v1:{0}:{0}-games'.format(self.resource), args=[obj.id]))
        return {'count': count, 'resource_url': resource_url}

    def get_expansions(self, obj):
        count = obj.expansions.count()
        resource_url = urljoin(settings.BASE_API,
                               reverse('api-v1:{0}:{0}-expansions'.format(self.resource),
                                       args=[obj.id]))
        return {'count': count, 'resource_url': resource_url}
