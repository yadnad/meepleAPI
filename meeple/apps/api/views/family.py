from django.conf.urls import url

from rest_framework import generics

from apps.api.models import Family
from apps.api.serializers.family import FamilySerializer, FamilyListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseDetailView, BaseListView


class FamilyListView(BaseListView):
    """
    Get list of families
    """
    queryset = Family.objects.all()
    serializer_class = FamilyListSerializer
    resource = 'families'


class FamilyDetailView(BaseDetailView):
    """
    Get family by ID
    """
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    resource = 'families'


class FamilyGamesView(BaseGameView):
    """
    Get list of games from this family
    """
    klass = Family
    resource = 'families'


class FamilyExpansionsView(BaseExpansionsView):
    """
    Get list of expansions from this family
    """
    klass = Family
    resource = 'families'

family_list = FamilyListView.as_view()
family_detail = FamilyDetailView.as_view()
family_games = FamilyGamesView.as_view()
family_expansions = FamilyExpansionsView.as_view()

urlpatterns = [
    url(r'^$', family_list, name='family-list'),
    url(r'^(?P<pk>[0-9]+)/$', family_detail, name='family-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', family_games, name='family-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', family_expansions, name='family-expansions'),
]