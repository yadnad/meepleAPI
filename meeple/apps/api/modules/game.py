import re
from django.utils.text import slugify

from apps.api.models import *


def add_integrations(game):
    geek_ids = set([game.get('objectid')])
    for x in game.get('boardgameintegration'):
        geek_ids.add(x.get('objectid'))

    games = Game.objects.filter(geek__object_id__in=geek_ids)
    games_ids = {x.id for x in games}

    for x in games_ids:
        other_games_ids = games_ids.copy()
        other_games_ids.remove(x)
        main_game = Game.objects.get(id=x)
        for o in other_games_ids:
            integration_game = Game.objects.get(id=o)
            main_game.integrations.add(integration_game)

    return True


def add_expansions(game):
    try:
        g = Game.objects.get(geek__object_id=game.get('objectid'))
    except Game.DoesNotExist:
        save_game(game)
        try:
            g = Game.objects.get(geek__object_id=game.get('objectid'))
        except Game.DoesNotExist:
            return False
    for x in game.get('boardgameexpansion'):
        try:
            game_expansion = Expansion.objects.get(geek__object_id=x.get('objectid'))
            g.expansions.add(game_expansion)
        except Expansion.DoesNotExist:
            pass

    return True


def add_ranking(game):
    try:
        geek = Geek.objects.get(object_id=game.get('objectid'))
    except Geek.DoesNotExist:
        save_game(game)
        try:
            geek = Geek.objects.get(object_id=game.get('objectid'))
        except Geek.DoesNotExist:
            return False
    if game.get('bgg_ranking'):
        for name, rank in game.get('bgg_ranking').iteritems():
            Rank.objects.create(name=name, rank=rank, geek=geek, rating=game.get('averagerating'))

    return True


def save_game(game):
    if Geek.objects.filter(object_id=game.get('objectid')).exists():
        return False

    if not game.get('name'):
        return False

    try:
        name = game.get('name')
        name = slugify(unicode(name))
    except:
        print '====================='
        print "Can't get slug: {0} {1}".format(game.get('objectid'), game.get('name'))
        print '====================='
        return False

    if not name:
        return False

    # create Geek
    bgg = Geek()
    bgg.ranking = game.get('rank')
    bgg.url = game.get('url')
    bgg.average_rating = game.get('averagerating')
    bgg.num_ratings = game.get('numratings')
    bgg.fans = game.get('fans')
    bgg.language_dependence = game.get('language_dependence') if game.get(
        'language_dependence') else None
    bgg.total_plays = game.get('totalplays')
    bgg.plays_this_month = game.get('playsthismonth')
    bgg.users_owning = game.get('usersowning')
    bgg.users_trading = game.get('userstrading')
    bgg.users_wanting = game.get('userswanting')
    bgg.object_id = game.get('objectid')
    suggested_age = game.get('suggested_playerage') or game.get('age')
    if suggested_age:
        age = int(re.search('(\d+)', str(suggested_age)).group(1))
    else:
        age = None
    bgg.suggested_age = age
    bgg.save()
    print 'Save Geek'

    if game.get('suggested_numplayers'):
        suggested_numplayers = game.get('suggested_numplayers')
        recommended = suggested_numplayers.get('Recommended') or []
        not_recommended = suggested_numplayers.get('Not Recommended') or []
        best = suggested_numplayers.get('Best') or []
        GeekPlayers.objects.create(recommended=recommended,
                                   not_recommended=not_recommended,
                                   best=best,
                                   geek=bgg)

    if game.get('expansion'):
        # create Expansion
        g = Expansion()
        g.name = game.get('name')
        g.age = game.get('age')
        g.year_published = game.get('yearpublished')
        g.playing_time = game.get('playingtime')

        g.max_players = game.get('maxplayers')
        g.min_players = game.get('minplayers')

        g.image = game.get('image')
        g.thumbnail = game.get('thumbnail')

        g.geek = bgg
        g.save()
        print 'Save Expansion'

    else:
        # create Game
        g = Game()
        g.name = game.get('name')
        g.age = game.get('age')
        g.year_published = game.get('yearpublished')
        g.playing_time = game.get('playingtime')

        g.language_dependence = game.get('language_dependence') if game.get(
            'language_dependence') else None
        g.max_players = game.get('maxplayers')
        g.min_players = game.get('minplayers')

        g.image = game.get('image')
        g.thumbnail = game.get('thumbnail')

        g.geek = bgg
        g.save()
        print 'Save Game'

    # create categories
    list_of = ['boardgamecategory', 'boardgamedesigner', 'boardgameartist',
               'boardgamepublisher',
               'boardgamemechanic', 'boardgamesubdomain', 'boardgamefamily']
    for cat in list_of:
        item = game.get(cat)
        if item:
            _get_data(g, item, cat)

    return True


def _get_data(g, item, meta):
    if 'artist' in meta:
        c = Artist
        insert = g.artists
    elif 'designer' in meta:
        c = Designer
        insert = g.designers
    elif 'publisher' in meta:
        c = Publisher
        insert = g.publishers
    elif 'category' in meta:
        c = Category
        insert = g.categories
    elif 'mechanic' in meta:
        c = Mechanic
        insert = g.mechanics
    elif 'subdomain' in meta:
        c = Subdomain
        insert = g.subdomains
    elif 'family' in meta:
        c = Family
        insert = g.families
    else:
        return False

    for x in item:
        name = x.get('name') or ''
        name = name.strip()
        try:
            name = slugify(unicode(name))
        except:
            print '====================='
            print "Can't get slug: {0} {1}".format(x.get('objectid'), x.get('name'))
            print '====================='
            continue
        object_id = x.get('objectid')
        if name:
            try:
                data = c.objects.get(object_id=object_id)
                insert.add(data)
            except c.DoesNotExist:
                data = c.objects.create(name=name, object_id=object_id)
                insert.add(data)
