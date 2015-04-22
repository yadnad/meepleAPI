def get_singular(key):
    properties = {
        'artists': 'artist',
        'designers': 'designer',
        'publishers': 'publisher',
        'categories': 'category',
        'subdomains': 'subdomain',
        'mechanics': 'mechanic',
        'families': 'family',
        'integrations': 'game',
        'expansions': 'expansion',
        'games': 'game'
    }
    return properties[key]


def get_plural(key):
    properties = {
        'artist': 'artists',
        'designer': 'designers',
        'publisher': 'publishers',
        'category': 'categories',
        'subdomain': 'subdomains',
        'mechanic': 'mechanics',
        'family': 'families',
        'integration': 'games',
        'expansion': 'expansions',
        'game': 'games'
    }
    return properties[key]
