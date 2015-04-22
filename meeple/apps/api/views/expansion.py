from django.conf.urls import url

from apps.api.models import Expansion
from apps.api.serializers.game import (ExpansionSerializer, ExpansionFullSerializer,
                                       ExpansionListSerializer)
from apps.api.views.helpers import BaseGeekView, BaseListView, BaseDetailView


class ExpansionListView(BaseListView):
    """
    Get list of expansions
    """
    # serializer_class = ExpansionSerializer
    resource = 'expansions'

    def get_queryset(self):
        queryset = Expansion.objects.all()
        object_id = self.request.QUERY_PARAMS.get('object_id', None)
        if object_id is not None:
            queryset = queryset.filter(geek__object_id__in=object_id.split(','))
        return queryset

    def get_serializer_class(self):
        view = self.request.QUERY_PARAMS.get('view', None)
        if view == 'full':
            return ExpansionFullSerializer
        elif view == 'small':
            return ExpansionListSerializer
        return ExpansionSerializer


class ExpansionDetailView(BaseDetailView):
    """
    Get expansion by ID
    """
    queryset = Expansion.objects.all()
    serializer_class = ExpansionFullSerializer
    resource = 'expansions'


class GeekDetailView(BaseGeekView):
    klass = Expansion
    resource = 'expansions'


expansion_list = ExpansionListView.as_view()
expansion_detail = ExpansionDetailView.as_view()
geek_detail = GeekDetailView.as_view()

urlpatterns = [
    url(r'^$', expansion_list, name='expansion-list'),
    url(r'^(?P<pk>[0-9]+)/$', expansion_detail, name='expansion-detail'),
    url(r'^(?P<pk>[0-9]+)/geek/$', geek_detail, name='geek-detail'),
]