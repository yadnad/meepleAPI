from django.conf.urls import url

from apps.api.models import Game
from apps.api.serializers.game import GameSerializer, GameFullSerializer, GameListSerializer
from apps.api.views.helpers import BaseGeekView, BaseListView, BaseDetailView


class GameListView(BaseListView):
    """
    Get list of games
    """
    resource = 'games'

    def get_queryset(self):
        queryset = Game.objects.all()
        object_id = self.request.QUERY_PARAMS.get('object_id', None)
        if object_id is not None:
            queryset = queryset.filter(geek__object_id__in=object_id.split(','))
        return queryset

    def get_serializer_class(self):
        view = self.request.QUERY_PARAMS.get('view', None)
        if view == 'full':
            return GameFullSerializer
        elif view == 'small':
            return GameListSerializer
        return GameSerializer


class GameDetailView(BaseDetailView):
    """
    Get game by ID
    """
    queryset = Game.objects.all()
    serializer_class = GameFullSerializer
    resource = 'games'


class GeekDetailView(BaseGeekView):
    """
    Get BGG data
    """
    klass = Game
    resource = 'games'


game_list = GameListView.as_view()
game_detail = GameDetailView.as_view()
geek_detail = GeekDetailView.as_view()

urlpatterns = [
    url(r'^$', game_list, name='game-list'),
    url(r'^(?P<pk>[0-9]+)/$', game_detail, name='game-detail'),
    url(r'^(?P<pk>[0-9]+)/geek/', geek_detail, name='geek-detail'),
]