from django.views.generic import TemplateView

from apps.api.models import (Game,
                             Expansion,
                             Designer,
                             Publisher,
                             Artist,
                             Category,
                             Subdomain,
                             Family,
                             Mechanic)
from apps.utils.resources import get_plural


class HomeView(TemplateView):
    template_name = "web/home.jinja"


class AboutView(TemplateView):
    template_name = "web/about.jinja"

    def _get_stats(self):
        stats = []
        klasses = [
            Game,
            Expansion,
            Designer,
            Publisher,
            Artist,
            Category,
            Subdomain,
            Family,
            Mechanic,
        ]
        for resource in klasses:
            stats.append(dict(count=resource.objects.count(),
                              resource=get_plural(resource.__name__.lower())))
        return stats


    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['stats'] = self._get_stats()
        return context


class DonateView(TemplateView):
    template_name = "web/donate.jinja"


class DocsView(TemplateView):
    template_name = "docs/base.jinja"
