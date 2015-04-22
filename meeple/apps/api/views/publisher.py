from django.conf.urls import url

from apps.api.models import Publisher
from apps.api.serializers.publisher import PublisherSerializer, PublisherListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseListView, BaseDetailView


class PublisherListView(BaseListView):
    """
    Get list of publishers
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer
    resource = 'publishers'


class PublisherDetailView(BaseDetailView):
    """
    Get publisher by ID
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    resource = 'publishers'


class PublisherGamesView(BaseGameView):
    """
    Get list of games from this publisher
    """
    klass = Publisher
    resource = 'publishers'


class PublisherExpansionsView(BaseExpansionsView):
    """
    Get list of expansions from this publisher
    """
    klass = Publisher
    resource = 'publishers'


publisher_list = PublisherListView.as_view()
publisher_detail = PublisherDetailView.as_view()
publisher_games = PublisherGamesView.as_view()
publisher_expansions = PublisherExpansionsView.as_view()

urlpatterns = [
    url(r'^$', publisher_list, name='publisher-list'),
    url(r'^(?P<pk>[0-9]+)/$', publisher_detail, name='publisher-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', publisher_games, name='publisher-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', publisher_expansions, name='publisher-expansions'),
]