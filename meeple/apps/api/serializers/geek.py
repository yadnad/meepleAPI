from __future__ import unicode_literals
from urlparse import urljoin

from django.conf import settings
from django.core.urlresolvers import reverse

from rest_framework import serializers

from apps.api.models import Rank, GeekPlayers, Geek, Game, Expansion


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ('name', 'rank', 'rating',)


class GeekPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekPlayers
        fields = ('best', 'recommended', 'not_recommended',)


class GeekListSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    suggested_players = GeekPlayersSerializer(many=True)

    def get_resource_url(self, obj):
        try:
            o = Game.objects.get(geek=obj.id)
            return urljoin(settings.BASE_API, reverse('api-v1:game:geek-detail',
                                                      args=[o.id]))
        except Game.DoesNotExist:
            o = Expansion.objects.get(geek=obj.id)
            return urljoin(settings.BASE_API, reverse('api-v1:expansion:geek-detail',
                                                      args=[o.id]))

    class Meta:
        model = Geek
        fields = ('resource_url', 'ranking', 'suggested_players', 'suggested_age',
                  'language_dependence', 'object_id')


class GeekSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    rank = RankSerializer(many=True)
    suggested_players = GeekPlayersSerializer(many=True)


    def get_resource_url(self, obj):
        try:
            o = Game.objects.get(geek=obj.id)
            return urljoin(settings.BASE_API, reverse('api-v1:game:geek-detail',
                                                      args=[o.id]))
        except Game.DoesNotExist:
            o = Expansion.objects.get(geek=obj.id)
            return urljoin(settings.BASE_API, reverse('api-v1:expansion:geek-detail',
                                                      args=[o.id]))

    class Meta:
        model = Geek
