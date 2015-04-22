from django.conf.urls import url

from apps.api.models import Artist
from apps.api.serializers.artist import ArtistSerializer, ArtistListSerializer
from apps.api.views.helpers import BaseDetailView, BaseExpansionsView, BaseGameView, BaseListView


class ArtistListView(BaseListView):
    """
    Get list of artists
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer
    resource = 'artists'


class ArtistDetailView(BaseDetailView):
    """
    Get artist by ID
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    resource = 'artists'


class ArtistGamesView(BaseGameView):
    """
    Get list of games from this artist
    """
    klass = Artist
    resource = 'artists'


class ArtistExpansionsView(BaseExpansionsView):
    """
    Get list of expansions from this artist
    """
    klass = Artist
    resource = 'artists'


artist_list = ArtistListView.as_view()
artist_detail = ArtistDetailView.as_view()
artist_games = ArtistGamesView.as_view()
artist_expansions = ArtistExpansionsView.as_view()

urlpatterns = [
    url(r'^$', artist_list, name='artist-list'),
    url(r'^(?P<pk>[0-9]+)/$', artist_detail, name='artist-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', artist_games, name='artist-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', artist_expansions, name='artist-expansions'),
]