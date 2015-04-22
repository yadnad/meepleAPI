import operator

import pyquery
import re
import requests

import xml.etree.ElementTree as ET


def get_games_ids(start_games, number_of_games):
    start_page = int(round(start_games/100.00))
    pages = int(round(number_of_games/100.00))
    pages += start_page
    ids = []
    for page in range(start_page, pages):
        response = requests.get('http://boardgamegeek.com/browse/boardgame/page/{0}'.format(page + 1)).text
        pq = pyquery.PyQuery(response)
        for x in pq('div[id^="results_objectname"] a').items():
            i = re.search('\/(boardgame|boardgameexpansion)\/(\d+)\/', x.attr('href'))
            if i:
                ids.append(int(i.group(2)))
    return ids[:number_of_games]


def get_game_info(game_id):
    game = get_game_info_from_site(game_id)
    if game:
        game.update(get_game_info_from_api(game['objectid']))
    return game


def get_game_info_from_site(game_id):
    response = requests.get('http://boardgamegeek.com/boardgame/{0}'.format(game_id))

    if 'rpgitem' in response.url:
        return None

    if response.status_code == 200:
        q = pyquery.PyQuery(response.text)
        item = dict()
        try:
            item['objectid'] = int(response.url.split('/')[-2])
            item['id'] = item['objectid']
        except:
            return None

        stats = {}
        if q('#results_17 .moduletable .module_title').text() == 'Statistics':
            for x in q('#module_17 .innermoduletable table tr').items():
                value = q(x).find('td').eq(0).text().encode("ascii", "ignore").replace(':', '')
                stats[value] = q(x).find('td').eq(1).text()
        elif q('#results_16 .moduletable .module_title').text() == 'Statistics':
            for x in q('#module_16 .innermoduletable table tr').items():
                value = q(x).find('td').eq(0).text().encode("ascii", "ignore").replace(':', '')
                stats[value] = q(x).find('td').eq(1).text()

        item['totalplays'] = int(stats['TotalPlays']) if stats['TotalPlays'] else 0
        item['averagerating'] = float(stats['Average Rating']) if stats['Average Rating'] else 0
        item['numviews'] = int(stats['Num Views']) if stats['Num Views'] else 0
        item['playsthismonth'] = int(stats['PlaysThisMonth']) if stats['PlaysThisMonth'] else 0
        item['userswanting'] = int(stats['UsersWanting']) if stats['UsersWanting'] else 0
        if stats['UsersTrading'] != '[find trade matches]':
            item['userstrading'] = int(stats['UsersTrading'].split('[')[0].strip())
        else:
            item['userstrading'] = 0
        item['numratings'] = float(stats['Num Ratings']) if stats['Num Ratings'] else 0
        item['avggameweight'] = float(stats['Avg.GameWeight']) if stats['Avg.GameWeight'] else 0
        item['usersowning'] = int(stats['UsersOwning']) if stats['UsersOwning'] else 0
        item['fans'] = int(stats['Fans']) if stats['Fans'] else 0

        rank = {}
        for x in stats.keys():
            if 'game rank' in x.lower():
                if stats[x] == 'N/A':
                    rank[x] = None
                else:
                    rank[x] = int(stats[x])

        item['bgg_ranking'] = rank
        item['rank'] = rank.get('Board Game Rank')
        item['url'] = response.url
        return item
    return None


def get_game_info_from_api(game_id):
    url = "http://www.boardgamegeek.com/xmlapi/boardgame/{0}".format(game_id)
    response = requests.get(url).text.encode("ascii", "ignore")
    root = ET.fromstring(response)
    return _get_game_info(root)


def _get_game_info(root):
    for boardgame in root.findall('boardgame'):
        item = {}
        if not boardgame.attrib.get('objectid'):
            return False
        item['objectid'] = int(boardgame.attrib['objectid'])
        # get suggested number of players poll
        suggested_numplayers = []
        poll = boardgame.find('poll[@name="suggested_numplayers"]')
        for x in poll.findall('results'):
            itm = x.attrib
            results = []
            for r in x.findall('result'):
                results.append(r.attrib)
            itm['results'] = results
            suggested_numplayers.append(itm)
        item['suggested_numplayers_raw'] = suggested_numplayers

        # get language dependence poll
        language_dependence = []
        poll = boardgame.find('poll[@name="language_dependence"]')
        for x in poll.findall('results'):
            for r in x.findall('result'):
                language_dependence.append(r.attrib)
        item['language_dependence_raw'] = language_dependence

        # get suggested player age poll
        suggested_playerage = []
        poll = boardgame.find('poll[@name="suggested_playerage"]')
        for x in poll.findall('results'):
            for r in x.findall('result'):
                suggested_playerage.append(r.attrib)
        item['suggested_playerage_raw'] = suggested_playerage

        try:
            numplayers = {}
            for x in item['suggested_numplayers_raw']:
                tmp = {}
                for i in x['results']:
                    tmp[i['value']] = int(i['numvotes'])
                best = max(tmp.iteritems(), key=operator.itemgetter(1))[0]
                numplayers[x['numplayers']] = best

            suggested = {}
            for key in numplayers.keys():
                if numplayers[key] not in suggested:
                    suggested[numplayers[key]] = [key]
                else:
                    suggested[numplayers[key]].append(key)
            item['suggested_numplayers'] = suggested
        except:
            item['suggested_numplayers'] = None

        try:
            item['best_numplayers'] = int(suggested['Best'])
        except:
            item['best_numplayers'] = None

        item['yearpublished'] = _find_attrib(boardgame, 'yearpublished')
        item['minplayers'] = _find_attrib(boardgame, 'minplayers')
        item['maxplayers'] = _find_attrib(boardgame, 'maxplayers')
        item['playingtime'] = _find_attrib(boardgame, 'playingtime')
        item['age'] = _find_attrib(boardgame, 'age')
        item['name'] = boardgame.find('name[@primary="true"]').text
        item['description'] = boardgame.find('description').text
        try:
            item['thumbnail'] = boardgame.find('thumbnail').text
        except:
            item['thumbnail'] = 'http://cf.geekdo-images.com/images/pic1657689_t.jpg'
        try:
            item['image'] = boardgame.find('image').text
        except:
            item['image'] = 'http://cf.geekdo-images.com/images/pic1657689.jpg'

        item['names'] = _get_multiple_data(boardgame, 'name')
        item['honors'] = _get_multiple_data(boardgame, 'boardgamehonor')
        item['boardgamepublisher'] = _get_multiple_data_objects(boardgame, 'boardgamepublisher')
        item['boardgamedesigner'] = _get_multiple_data_objects(boardgame, 'boardgamedesigner')
        item['boardgameartist'] = _get_multiple_data_objects(boardgame, 'boardgameartist')
        item['boardgameexpansion'] = _get_multiple_data_objects(boardgame, 'boardgameexpansion')
        item['boardgamecategory'] = _get_multiple_data_objects(boardgame, 'boardgamecategory')
        item['boardgamemechanic'] = _get_multiple_data_objects(boardgame, 'boardgamemechanic')
        item['boardgamesubdomain'] = _get_multiple_data_objects(boardgame, 'boardgamesubdomain')
        item['boardgamefamily'] = _get_multiple_data_objects(boardgame, 'boardgamefamily')
        item['boardgameintegration'] = _get_multiple_data_objects(boardgame, 'boardgameintegration')

        item['language_dependence'] = _get_best_poll_result(item['language_dependence_raw'])
        item['suggested_playerage'] = _get_best_poll_result(item['suggested_playerage_raw'])

        item['base_game'] = _get_base_game(boardgame, 'boardgameexpansion')
        item['expansion'] = any(d.get('name', None) == 'Expansion for Base-game' for d in
                                item.get('boardgamecategory')) or item['base_game']


        return item


def _get_multiple_data(boardgame, params):
    items = []
    for item in boardgame.findall(params):
        items.append(item.text)
    return items


def _get_multiple_data_objects(boardgame, params):
    items = []
    for item in boardgame.findall(params):
        items.append({'name': item.text, 'objectid': item.attrib['objectid']})
    return items


def _get_base_game(boardgame, params):
    items = []
    for item in boardgame.findall(params):
        if item.attrib.get('inbound'):
            items.append({'name': item.text, 'objectid': item.attrib['objectid']})
    return items


def _get_best_poll_result(item):
    data = {}
    result = None
    for x in item:
        data[x['value']] = int(x['numvotes'])
        result = max(data.iteritems(), key=operator.itemgetter(1))[0]
    return result


def _find_attrib(boardgame, attrib):
    data = boardgame.find(attrib).text
    if data is not None:
        return int(data)
    return None