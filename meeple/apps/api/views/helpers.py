from rest_framework import generics

from django.shortcuts import get_object_or_404

from apps.api.serializers.game import ExpansionSerializer, GameSerializer
from apps.api.serializers.geek import GeekSerializer
from apps.utils.analytics import keen_hit


class BaseExpansionsView(generics.ListAPIView):
    """

    """
    serializer_class = ExpansionSerializer
    lookup_url_kwarg = "pk"
    klass = None
    resource = None

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        obj = get_object_or_404(self.klass, pk=pk)
        return obj.expansions

    def dispatch(self, request, *args, **kwargs):
        keen_hit('expansions-list', self.resource, request)
        return super(BaseExpansionsView, self).dispatch(request, *args, **kwargs)


class BaseGameView(generics.ListAPIView):
    """

    """
    serializer_class = GameSerializer
    lookup_url_kwarg = "pk"
    klass = None
    resource = None

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        obj = get_object_or_404(self.klass, pk=pk)
        return obj.games

    def dispatch(self, request, *args, **kwargs):
        keen_hit('games-list', self.resource, request)
        return super(BaseGameView, self).dispatch(request, *args, **kwargs)


class BaseGeekView(generics.RetrieveAPIView):
    """
    Get BGG data
    """
    serializer_class = GeekSerializer
    lookup_url_kwarg = "pk"
    klass = None
    resource = None

    def get_object(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        obj = get_object_or_404(self.klass, pk=pk)
        return obj.geek

    def dispatch(self, request, *args, **kwargs):
        keen_hit('geek', self.resource, request)
        return super(BaseGeekView, self).dispatch(request, *args, **kwargs)


class BaseListView(generics.ListAPIView):
    resource = None

    def dispatch(self, request, *args, **kwargs):
        keen_hit('list', self.resource, request)
        return super(BaseListView, self).dispatch(request, *args, **kwargs)


class BaseDetailView(generics.RetrieveAPIView):
    resource = None

    def dispatch(self, request, *args, **kwargs):
        keen_hit('detail', self.resource, request)
        return super(BaseDetailView, self).dispatch(request, *args, **kwargs)