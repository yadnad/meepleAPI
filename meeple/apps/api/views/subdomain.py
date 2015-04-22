from django.conf.urls import url

from apps.api.models import Subdomain
from apps.api.serializers.subdomain import SubdomainSerializer, SubdomainListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseListView, BaseDetailView


class SubdomainListView(BaseListView):
    """
    Get list of subdomains
    """
    queryset = Subdomain.objects.all()
    serializer_class = SubdomainListSerializer
    resource = 'subdomains'


class SubdomainDetailView(BaseDetailView):
    """
    Get subdomain by ID
    """
    queryset = Subdomain.objects.all()
    serializer_class = SubdomainSerializer
    resource = 'subdomains'


class SubdomainGamesView(BaseGameView):
    """
    Get list of games with this subdomain
    """
    klass = Subdomain
    resource = 'subdomains'


class SubdomainExpansionsView(BaseExpansionsView):
    """
    Get list of expansions with this subdomain
    """
    klass = Subdomain
    resource = 'subdomains'


subdomain_list = SubdomainListView.as_view()
subdomain_detail = SubdomainDetailView.as_view()
subdomain_games = SubdomainGamesView.as_view()
subdomain_expansions = SubdomainExpansionsView.as_view()

urlpatterns = [
    url(r'^$', subdomain_list, name='subdomain-list'),
    url(r'^(?P<pk>[0-9]+)/$', subdomain_detail, name='subdomain-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', subdomain_games, name='subdomain-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', subdomain_expansions, name='subdomain-expansions'),
]