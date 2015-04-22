from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Subdomain


class SubdomainListSerializer(base.BasePropertiesListSerializer):
    resource = 'subdomain'

    class Meta:
        model = Subdomain
        fields = base.LIST_FIELDS


class SubdomainSerializer(base.BasePropertiesDetailSerializer):
    resource = 'subdomain'

    class Meta:
        model = Subdomain
        fields = base.DETAIL_FIELDS