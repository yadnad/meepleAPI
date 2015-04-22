from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Mechanic


class MechanicListSerializer(base.BasePropertiesListSerializer):
    resource = 'mechanic'

    class Meta:
        model = Mechanic
        fields = base.LIST_FIELDS


class MechanicSerializer(base.BasePropertiesDetailSerializer):
    resource = 'mechanic'

    class Meta:
        model = Mechanic
        fields = base.DETAIL_FIELDS