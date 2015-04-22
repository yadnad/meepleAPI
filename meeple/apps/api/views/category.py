from django.conf.urls import url

from apps.api.models import Category
from apps.api.serializers.category import CategorySerializer, CategoryListSerializer
from apps.api.views.helpers import BaseGameView, BaseExpansionsView, BaseListView, BaseDetailView


class CategoryListView(BaseListView):
    """
    Get list of categories
    """
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    resource = 'categories'


class CategoryDetailView(BaseDetailView):
    """
    Get category by ID
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    resource = 'categories'


class CategoryGamesView(BaseGameView):
    """
    Get list of games with this category
    """
    klass = Category
    resource = 'categories'


class CategoryExpansionsView(BaseExpansionsView):
    """
    Get list of expansions with this category
    """
    klass = Category
    resource = 'categories'


category_list = CategoryListView.as_view()
category_detail = CategoryDetailView.as_view()
category_games = CategoryGamesView.as_view()
category_expansions = CategoryExpansionsView.as_view()

urlpatterns = [
    url(r'^$', category_list, name='category-list'),
    url(r'^(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    url(r'^(?P<pk>[0-9]+)/games/$', category_games, name='category-games'),
    url(r'^(?P<pk>[0-9]+)/expanisons/$', category_expansions, name='category-expansions'),
]