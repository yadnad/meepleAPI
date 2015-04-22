import time

from django.core.management.base import BaseCommand

from apps.utils.scraper import boardgamegeek as games
from apps.api.modules.game import save_game


class Command(BaseCommand):
    help = 'Get top games and save then to db'

    def add_arguments(self, parser):
        parser.add_argument('game_id', type=int)

    def handle(self, **options):
        game_id = options['game_id']

        game = games.get_game_info(game_id)
        print game
        # if game:
        #     self._get_expansion(game)
        #     self._get_integrations(game)
        #     save_game(game)
        #     add_integrations(game)
        #     self.stdout.write('Added {0}: {1}'.format(game['name'], game['rank']))
        #     time.sleep(1)



    def _get_expansion(self, game):
        for x in game.get('boardgameexpansion'):
            game = games.get_game_info(x.get('objectid'))
            if game:
                save_game(game)
                self.stdout.write('Added expansion {0}: {1}'.format(game['name'], game['rank']))
                time.sleep(1)
            else:
                self.stdout.write('=====================')
                self.stdout.write('Problem with adding {0}'.format(x.get('objectid')))
                self.stdout.write('=====================')
                continue

    def _get_integrations(self, game):
        for x in game.get('boardgameintegration'):
            game = games.get_game_info(x.get('objectid'))
            if game:
                save_game(game)
                self.stdout.write('Added integration {0}: {1}'.format(game['name'], game['rank']))
                time.sleep(1)
            else:
                self.stdout.write('=====================')
                self.stdout.write('Problem with adding {0}'.format(x.get('objectid')))
                self.stdout.write('=====================')
                continue