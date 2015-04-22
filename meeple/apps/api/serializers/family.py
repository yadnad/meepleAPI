from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Family


class FamilyListSerializer(base.BasePropertiesListSerializer):
    resource = 'family'

    class Meta:
        model = Family
        fields = base.LIST_FIELDS


class FamilySerializer(base.BasePropertiesDetailSerializer):
    resource = 'family'

    class Meta:
        model = Family
        fields = base.DETAIL_FIELDS