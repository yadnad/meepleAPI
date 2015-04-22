from django.conf.urls import url

from apps.api.models import Designer
from apps.api.serializers.designer import DesignerSerializer, DesignerListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseListView, BaseDetailView


class DesignerListView(BaseListView):
    """
    Get list of designers
    """
    queryset = Designer.objects.all()
    serializer_class = DesignerListSerializer
    resource = 'designers'


class DesignerDetailView(BaseDetailView):
    """
    Get designer by ID
    """
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer
    resource = 'designers'


class DesignerGamesView(BaseGameView):
    """
    Get list of games from this designer
    """
    klass = Designer
    resource = 'designers'


class DesignerExpansionsView(BaseExpansionsView):
    """
    Get list of expansions from this designer
    """
    klass = Designer
    resource = 'designers'


designer_list = DesignerListView.as_view()
designer_detail = DesignerDetailView.as_view()
designer_games = DesignerGamesView.as_view()
designer_expansions = DesignerExpansionsView.as_view()

urlpatterns = [
    url(r'^$', designer_list, name='designer-list'),
    url(r'^(?P<pk>[0-9]+)/$', designer_detail, name='designer-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', designer_games, name='designer-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', designer_expansions, name='designer-expansions'),
]