from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Publisher


class PublisherListSerializer(base.BasePropertiesListSerializer):
    resource = 'publisher'

    class Meta:
        model = Publisher
        fields = base.LIST_FIELDS


class PublisherSerializer(base.BasePropertiesDetailSerializer):
    resource = 'publisher'

    class Meta:
        model = Publisher
        fields = base.DETAIL_FIELDS