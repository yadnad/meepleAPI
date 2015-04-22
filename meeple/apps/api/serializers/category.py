from __future__ import unicode_literals

from apps.api.serializers import base
from apps.api.models import Category


class CategoryListSerializer(base.BasePropertiesListSerializer):
    resource = 'category'

    class Meta:
        model = Category
        fields = base.LIST_FIELDS


class CategorySerializer(base.BasePropertiesDetailSerializer):
    resource = 'category'

    class Meta:
        model = Category
        fields = base.DETAIL_FIELDS