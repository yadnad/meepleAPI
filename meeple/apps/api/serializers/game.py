from __future__ import unicode_literals

from urlparse import urljoin

from django.conf import settings
from django.core.urlresolvers import reverse

from rest_framework import serializers

from apps.api.serializers import (artist, base, category, designer, family, geek,
                                  mechanic, publisher, subdomain)
from apps.api.models import Game
from apps.api.models import Expansion


class GameListSerializer(base.BasePropertiesListSerializer):
    resource = 'game'

    class Meta:
        model = Game
        fields = base.LIST_FIELDS


class ExpansionListSerializer(base.BasePropertiesListSerializer):
    resource = 'expansion'

    class Meta:
        model = Expansion
        fields = base.LIST_FIELDS


class ExpansionFullSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    artists = artist.ArtistListSerializer(many=True)
    designers = designer.DesignerListSerializer(many=True)
    publishers = publisher.PublisherListSerializer(many=True)
    mechanics = mechanic.MechanicListSerializer(many=True)
    subdomains = subdomain.SubdomainListSerializer(many=True)
    categories = category.CategoryListSerializer(many=True)
    families = family.FamilyListSerializer(many=True)
    geek = geek.GeekListSerializer()
    games = GameListSerializer(many=True)

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:expansion:expansion-detail',
                                                  args=[obj.id]))

    class Meta:
        model = Expansion
        fields = (
            'resource_url',
            'name',
            'slug',
            'age',
            'year_published',
            'playing_time',
            'players',
            'min_players',
            'max_players',
            'image',
            'thumbnail',
            'date_updated',
            'date_added',
            'geek',
            'artists',
            'designers',
            'publishers',
            'categories',
            'subdomains',
            'mechanics',
            'families',
            'games')


class ExpansionSerializer(serializers.HyperlinkedModelSerializer):
    resource_url = serializers.SerializerMethodField()
    geek = geek.GeekListSerializer()

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:expansion:expansion-detail',
                                                  args=[obj.id]))

    class Meta:
        model = Expansion
        fields = (
            'resource_url',
            'name',
            'age',
            'year_published',
            'playing_time',
            'players',
            'image',
            'thumbnail',
            'geek')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    geek = geek.GeekListSerializer()

    resource_url = serializers.SerializerMethodField()

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:game:game-detail', args=[obj.id]))

    class Meta:
        model = Game
        fields = (
            'resource_url',
            'name',
            'age',
            'year_published',
            'playing_time',
            'players',
            'image',
            'thumbnail',
            'geek',
        )

class GameFullSerializer(serializers.HyperlinkedModelSerializer):
    artists = artist.ArtistListSerializer(many=True)
    designers = designer.DesignerListSerializer(many=True)
    publishers = publisher.PublisherListSerializer(many=True)
    mechanics = mechanic.MechanicListSerializer(many=True)
    subdomains = subdomain.SubdomainListSerializer(many=True)
    categories = category.CategoryListSerializer(many=True)
    families = family.FamilyListSerializer(many=True)
    geek = geek.GeekListSerializer()
    expansions = ExpansionListSerializer(many=True)
    integrations = GameListSerializer(many=True)

    resource_url = serializers.SerializerMethodField()

    def get_resource_url(self, obj):
        return urljoin(settings.BASE_API, reverse('api-v1:game:game-detail', args=[obj.id]))

    class Meta:
        model = Game
        fields = (
            'resource_url',
            'name',
            'slug',
            'age',
            'year_published',
            'playing_time',
            'players',
            'min_players',
            'max_players',
            'image',
            'thumbnail',
            'date_updated',
            'date_added',
            'geek',
            'artists',
            'designers',
            'publishers',
            'categories',
            'subdomains',
            'mechanics',
            'families',
            'expansions',
            'integrations',
        )


