from django.conf.urls import url

from apps.api.models import Mechanic
from apps.api.serializers.mechanic import MechanicSerializer, MechanicListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseListView, BaseDetailView


class MechanicListView(BaseListView):
    """
    Get list of mechanics
    """
    queryset = Mechanic.objects.all()
    serializer_class = MechanicListSerializer
    resource = 'mechanics'


class MechanicDetailView(BaseDetailView):
    """
    Get mechanic by ID
    """
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    resource = 'mechanics'


class MechanicGamesView(BaseGameView):
    """
    Get list of games with this mechanic
    """
    klass = Mechanic
    resource = 'mechanics'


class MechanicExpansionsView(BaseExpansionsView):
    """
    Get list of expansions with this mechanic
    """
    klass = Mechanic
    resource = 'mechanics'


mechanic_list = MechanicListView.as_view()
mechanic_detail = MechanicDetailView.as_view()
mechanic_games = MechanicGamesView.as_view()
mechanic_expansions = MechanicExpansionsView.as_view()

urlpatterns = [
    url(r'^$', mechanic_list, name='mechanic-list'),
    url(r'^(?P<pk>[0-9]+)/$', mechanic_detail, name='mechanic-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', mechanic_games, name='mechanic-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', mechanic_expansions, name='mechanic-expansions'),
]