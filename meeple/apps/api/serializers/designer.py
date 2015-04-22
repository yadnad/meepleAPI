from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Designer


class DesignerListSerializer(base.BasePropertiesListSerializer):
    resource = 'designer'

    class Meta:
        model = Designer
        fields = base.LIST_FIELDS


class DesignerSerializer(base.BasePropertiesDetailSerializer):
    resource = 'designer'

    class Meta:
        model = Designer
        fields = base.DETAIL_FIELDS