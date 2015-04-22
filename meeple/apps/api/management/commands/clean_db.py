from django.core.management.base import BaseCommand, CommandError

from apps.api.models import *

class Command(BaseCommand):
    help = 'Clean database'

    def handle(self, *args, **options):
        Geek.objects.all().delete()
        Game.objects.all().delete()
        Rank.objects.all().delete()
