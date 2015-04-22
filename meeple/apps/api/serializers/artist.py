from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Artist


class ArtistListSerializer(base.BasePropertiesListSerializer):
    resource = 'artist'

    class Meta:
        model = Artist
        fields = base.LIST_FIELDS


class ArtistSerializer(base.BasePropertiesDetailSerializer):
    resource = 'artist'

    class Meta:
        model = Artist
        fields = base.DETAIL_FIELDS