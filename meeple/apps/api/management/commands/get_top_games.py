import time

from django.core.management.base import BaseCommand

from apps.utils.scraper import boardgamegeek as games
from apps.api.models import Geek
from apps.api.modules.game import add_expansions, add_integrations, add_ranking, save_game


class Command(BaseCommand):
    help = 'Get top games and save then to db'

    def add_arguments(self, parser):
        parser.add_argument('start_pages', type=int)
        parser.add_argument('number_of_games', type=int)

    def handle(self, **options):
        number_of_games = options['number_of_games']
        start_pages = options['start_pages']
        for game_id in games.get_games_ids(start_pages, number_of_games):

            if Geek.objects.filter(object_id=game_id).exists():
                continue
            try:
                self.stdout.write('Processing {0}'.format(game_id))
                game = games.get_game_info(game_id)
            except Exception as e:
                self.stdout.write('=====================')
                self.stdout.write('Problem with adding {0}'.format(game_id))
                self.stdout.write(str(e))
                self.stdout.write('=====================')
                continue
            if game:
                for extra in ['boardgameexpansion', 'boardgameintegration']:
                    self._get_extra(game, extra)
                status = save_game(game)
                if status:
                    self.stdout.write('Added {0}: {1}'.format(game['name'], game['rank']))
                status = add_expansions(game)
                if status:
                    self.stdout.write('Added expansions')
                status = add_integrations(game)
                if status:
                    self.stdout.write('Added integrations')
                status = add_ranking(game)
                if status:
                    self.stdout.write('Added ranking')
                time.sleep(1.5)

    def _get_extra(self, game, extra):
        for x in game.get(extra):
            game = games.get_game_info(x.get('objectid'))
            if game:
                self.stdout.write('Processing {0}'.format(x.get('objectid')))
                status = save_game(game)
                if status:
                    self.stdout.write('Added {0} {1}: {2}'.format(extra, game['name'], game['rank']))
                else:
                    self.stdout.write('=====================')
                    self.stdout.write('Problem with adding {0}'.format(x.get('objectid')))
                    self.stdout.write('=====================')
                time.sleep(1.5)
            else:
                self.stdout.write('=====================')
                self.stdout.write('Problem with adding {0}'.format(x.get('objectid')))
                self.stdout.write('=====================')
                continue
