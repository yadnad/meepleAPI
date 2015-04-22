
#Documentation
- - -
<a name="intro"></a>
###Introduction

Welcome to the meepleAPI, RESTful board games API!

This documentation should help you familiarise yourself with the resources available and how to consume them with HTTP requests. Read through the getting started section before you dive in. Most of your problems should be solved just by reading through it.

<a name="authentication"></a>
###Authentication

meepleAPI is a completely open API. No authenitcation is required to query and get data. If you find a mistake in the data, then [tweet the author](https://twitter.com/MihaZelnik) or [email him](mailto:miha.zelnik@gmail.com).


<a name="rate"></a>
###Rate limiting

meepleAPI has rate limiting to prevent malicious abuse and to make sure our service can handle a potentially large amount of traffic. Rate limiting is done via IP address and is currently limited to 25,000 API request per day.


#Resources
- - -

<a name="root"></a>
##Root

The Root resource provides information on all available resources within the API.

**Example request:**

    http http://api.meeple.co/v1/

**Example response:**

    HTTP 200 OK
    Content-Type: application/json

    {
        "mechanics": "http://api.meeple.co/v1/mechanics/",
        "publishers": "http://api.meeple.co/v1/publishers/",
        "games": "http://api.meeple.co/v1/games/",
        "artists": "http://api.meeple.co/v1/artists/",
        "families": "http://api.meeple.co/v1/families/",
        "designers": "http://api.meeple.co/v1/designers/",
        "expansions": "http://api.meeple.co/v1/expansions/",
        "categories": "http://api.meeple.co/v1/categories/",
        "subdomains": "http://api.meeple.co/v1/subdomains/"
    }

**Attributes:**

- ```mechanics``` *string*
-- The URL root for mechanics
- ```publishers``` *string*
-- The URL root for publishers
- ```games``` *string*
-- The URL root for games
- ```artists``` *string*
-- The URL root for artists
- ```families``` *string*
-- The URL root for families
- ```designers``` *string*
-- The URL root for designers
- ```expansions``` *string*
-- The URL root for expansions
- ```categories``` *string*
-- The URL root for categories
- ```subdomains``` *string*
-- The URL root for subdomains


- - -
<a name="games"></a>
##Games

All board games (without expansions and promos)

###Endpoints

- ```/v1/games/``` -- get all board games
- ```/v1/games/:id/``` -- get a specific board game
- ```/v1/games/:id/geek/``` -- get stats from BGG for this game

###Filters

- ```/v1/games/?object_id=:object_id``` -- object_id is BGG id.
- ```/v1/games/?object_id=:object_id,object_id,object_id``` -- you can add multiple ids, they need to be seperate by `,`

This is used for mapping BGG games with this API. Because games and expansions are different resources you can get empty list back, because objects id is expansion and not game. In that case you need to do another request to expansions endpoint.

###Views

- ```/v1/games/?view=small``` -- get all board games with only *name* and *resource_url* fields
- ```/v1/games/?view=full``` -- get all board games with all fields (same as single game view)

**Example request:**

    http http://api.meeple.co/v1/games/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "resource_url": "http://api.meeple.co/v1/games/1/",
        "name": "Twilight Struggle",
        "slug": "twilight-struggle",
        "age": 13,
        "year_published": 2005,
        "playing_time": 180,
        "players": 2,
        "min_players": 2,
        "max_players": 2,
        "image": "//cf.geekdo-images.com/images/pic361592.jpg",
        "thumbnail": "//cf.geekdo-images.com/images/pic361592_t.jpg",
        "date_updated": "2015-04-11T12:44:13.516039Z",
        "date_added": "2015-04-11T12:44:13.516081Z",
        "geek": {
            "resource_url": "http://api.meeple.co/v1/games/1/geek/",
            "ranking": 1,
            "suggested_players": [
                {
                    "best": [
                        "2"
                    ],
                    "recommended": [],
                    "not_recommended": [
                        "1",
                        "2+"
                    ]
                }
            ],
            "suggested_age": 14,
            "language_dependence": "Extensive use of text - massive conversion needed to be playable",
            "object_id": 12333
        },
        "artists": [
            {
                "name": "Viktor Csete",
                "resource_url": "http://api.meeple.co/v1/artists/2/"
            },
            ...
        ],
        "designers": [
            {
                "name": "Ananda Gupta",
                "resource_url": "http://api.meeple.co/v1/designers/1/"
            },
            ...
        ],
        "publishers": [
            {
                "name": "GMT Games",
                "resource_url": "http://api.meeple.co/v1/publishers/4/"
            },
            ...
        ],
        "categories": [
            {
                "name": "Modern Warfare",
                "resource_url": "http://api.meeple.co/v1/categories/2/"
            },
            ...
        ],
        "subdomains": [
            {
                "name": "Strategy Games",
                "resource_url": "http://api.meeple.co/v1/subdomains/1/"
            },
            ...
        ],
        "mechanics": [
            {
                "name": "Area Control / Area Influence",
                "resource_url": "http://api.meeple.co/v1/mechanics/1/"
            },
            ...
        ],
        "families": [],
        "expansions": [
            {
                "name": "Twilight Struggle: What If?",
                "resource_url": "http://api.meeple.co/v1/expansions/4/"
            },
            ...
        ],
        "integrations": []
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this game *
- ```name``` *string* -- game name *
- ```slug``` *string* -- game slug
- ```age``` *int* -- player age *
- ```year_published``` *int* -- year when game was published *
- ```playing_time``` *int* -- playing time in minutes *
- ```players``` *string* -- number of players *
- ```min_players``` *int* -- minimum number of players
- ```max_players``` *int* -- maximum number of players
- ```image``` *string* -- image of board game box *
- ```thumbnail``` *string* -- small image of board game box *
- ```artists``` *array* -- An array of artists for this artist
- ```designers``` *array* -- An array of designers for this designer
- ```publishers``` *array* -- An array of publishers for this publisher
- ```categories``` *array* -- An array of categories for this category
- ```subdomains``` *array* -- An array of subdomains for this subdomain
- ```mechanics``` *array* -- An array of mechanics for this mechanic
- ```families``` *array* -- An array of families for this family
- ```expansions``` *array* -- An array of expansions for this expansion
- ```integrations``` *array* -- An array of integrations (other games) for this game
- ```geek``` *dictionary* -- few fields from Geek resource *
	- `resource_url` *string* -- hypermedia URL to Geek resource
	- `ranking` *int* -- BGG ranking (if None ranking don't exist)
	- `suggested_players` *array* -- list of best, recommended, not_recommended number of players based on voting on BGG
	- `suggested_age` *int* -- suggested player age based voting on BGG
	- `language_dependence` *string* -- how much is game language depended based voting on BGG
	- `object_id` *int* -- object_id is ID from BGG
- ```date_updated``` *string* -- date and time when this resources was last updated
- ```date_added``` *string* -- date and time when this resources was added

fields mark with `*` are in normal list view

- - -

<a name="expansions"></a>
##Expansions

All expansions and promos

###Endpoints

- ```/v1/expanisons/``` -- get all expanisons and promos
- ```/v1/expanisons/:id/``` -- get a specific expanison
- ```/v1/expanisons/:id/geek/``` -- get stats from BGG for this expanison

###Filters

- ```/v1/expanisons/?object_id=:object_id``` -- object_id is BGG id.
- ```/v1/expanisons/?object_id=:object_id,object_id,object_id``` -- you can add multiple ids, they need to be seperate by `,`

This is used for mapping BGG expanisons with this API. Because games and expansions are different resources you can get empty list back, because objects id is game and not expanison. In that case you need to do another request to games endpoint.

###Views

- ```/v1/expanisons/?view=small``` -- get all expanisons with only *name* and *resource_url* fields
- ```/v1/expanisons/?view=full``` -- get all expanisons with all fields (same as single expanison view)

**Example request:**

    http http://api.meeple.co/v1/expanisons/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "resource_url": "http://api.meeple.co/v1/expansions/1/",
        "name": "Twilight Struggle: \"Anni di Piombo\" Promo Card",
        "slug": "twilight-struggle-anni-di-piombo-promo-card",
        "age": 0,
        "year_published": 2011,
        "playing_time": 0,
        "players": 2,
        "min_players": 2,
        "max_players": 2,
        "image": "//cf.geekdo-images.com/images/pic1150389.jpg",
        "thumbnail": "//cf.geekdo-images.com/images/pic1150389_t.jpg",
        "date_updated": "2015-04-11T10:44:47.984965Z",
        "date_added": "2015-04-11T10:44:47.984985Z",
        "geek": {
            "resource_url": "http://api.meeple.co/v1/expansions/1/geek/",
            "ranking": null,
            "suggested_players": [
                {
                    "best": [],
                    "recommended": [
                        "1",
                        "2",
                        "2+"
                    ],
                    "not_recommended": []
                }
            ],
            "suggested_age": 0,
            "language_dependence": null,
            "object_id": 117145
        },
        "artists": [
            {
                "name": "(Uncredited)",
                "resource_url": "http://api.meeple.co/v1/artists/1/"
            }
        ],
        "designers": [
            {
                "name": "Ananda Gupta",
                "resource_url": "http://api.meeple.co/v1/designers/1/"
            },
            ...
        ],
        "publishers": [
            {
                "name": "Asterion Press",
                "resource_url": "http://api.meeple.co/v1/publishers/1/"
            },
            ...
        ],
        "categories": [
            {
                "name": "Expansion for Base-game",
                "resource_url": "http://api.meeple.co/v1/categories/1/"
            },
            ...
        ],
        "subdomains": [],
        "mechanics": [
            {
                "name": "Area Control / Area Influence",
                "resource_url": "http://api.meeple.co/v1/mechanics/1/"
            },
            ...
        ],
        "families": [
            {
                "name": "Promotional Cards",
                "resource_url": "http://api.meeple.co/v1/families/1/"
            }
        ],
        "games": [
            {
                "name": "Twilight Struggle",
                "resource_url": "http://api.meeple.co/v1/games/1/"
            }
        ]
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this game *
- ```name``` *string* -- game name *
- ```slug``` *string* -- game slug
- ```age``` *int* -- player age *
- ```year_published``` *int* -- year when game was published *
- ```playing_time``` *int* -- playing time in minutes *
- ```players``` *string* -- number of players *
- ```min_players``` *int* -- minimum number of players
- ```max_players``` *int* -- maximum number of players
- ```image``` *string* -- image of board game box *
- ```thumbnail``` *string* -- small image of board game box *
- ```artists``` *array* -- An array of artists for this artist
- ```designers``` *array* -- An array of designers for this designer
- ```publishers``` *array* -- An array of publishers for this publisher
- ```categories``` *array* -- An array of categories for this category
- ```subdomains``` *array* -- An array of subdomains for this subdomain
- ```mechanics``` *array* -- An array of mechanics for this mechanic
- ```families``` *array* -- An array of families for this family
- ```games``` *array* -- An array of base games for this expanisons
- ```geek``` *dictionary* -- few fields from Geek resource *
	- `resource_url` *string* -- hypermedia URL to Geek resource
	- `ranking` *int* -- BGG ranking (if None ranking don't exist)
	- `suggested_players` *array* -- list of best, recommended, not_recommended number of players based on voting on BGG
	- `suggested_age` *int* -- suggested player age based voting on BGG
	- `language_dependence` *string* -- how much is game language depended based voting on BGG
	- `object_id` *int* -- object_id is ID from BGG
- ```date_updated``` *string* -- date and time when this resources was last updated
- ```date_added``` *string* -- date and time when this resources was added

fields mark with `*` are in normal list view

- - -

<a name="artists"></a>
##Artists

All board game artists

###Endpoints

- ```/v1/artists/``` -- get all artists
- ```/v1/artists/:id/``` -- get a specific artist
- ```/v1/artists/:id/games/``` -- get list of games from this artist
- ```/v1/artists/:id/expansions/``` -- get list of expansions from this artist


**Example request:**

    http http://api.meeple.co/v1/artists/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "(Uncredited)",
        "slug": "uncredited",
        "resource_url": "http://api.meeple.co/v1/artists/1/",
        "games": {
            "count": 2787,
            "resource_url": "http://api.meeple.co/v1/artists/1/games/"
        },
        "expansions": {
            "count": 206,
            "resource_url": "http://api.meeple.co/v1/artists/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this artist
- ```name``` *string* -- artist name
- ```slug``` *string* -- artist slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="publishers"></a>
##Publishers

All board game publishers

###Endpoints

- ```/v1/publishers/``` -- get all publishers
- ```/v1/publishers/:id/``` -- get a specific publisher
- ```/v1/publishers/:id/games/``` -- get list of games from this publisher
- ```/v1/publishers/:id/expansions/``` -- get list of expansions from this publisher


**Example request:**

    http http://api.meeple.co/v1/publishers/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Asterion Press",
        "slug": "asterion-press",
        "resource_url": "http://api.meeple.co/v1/publishers/1/",
        "games": {
            "count": 79,
            "resource_url": "http://api.meeple.co/v1/publishers/1/games/"
        },
        "expansions": {
            "count": 34,
            "resource_url": "http://api.meeple.co/v1/publishers/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this publisher
- ```name``` *string* -- publisher name
- ```slug``` *string* -- publisher slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="designers"></a>
##Designers

All board game designers

###Endpoints

- ```/v1/designers/``` -- get all designers
- ```/v1/designers/:id/``` -- get a specific designer
- ```/v1/designers/:id/games/``` -- get list of games from this designer
- ```/v1/designers/:id/expansions/``` -- get list of expansions from this designer


**Example request:**

    http http://api.meeple.co/v1/designers/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Ananda Gupta",
        "slug": "ananda-gupta",
        "resource_url": "http://api.meeple.co/v1/designers/1/",
        "games": {
            "count": 1,
            "resource_url": "http://api.meeple.co/v1/designers/1/games/"
        },
        "expansions": {
            "count": 4,
            "resource_url": "http://api.meeple.co/v1/designers/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this designer
- ```name``` *string* -- designer name
- ```slug``` *string* -- designer slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="categories"></a>
##Categories

All board game categories

###Endpoints

- ```/v1/categories/``` -- get all categories
- ```/v1/categories/:id/``` -- get a specific category
- ```/v1/categories/:id/games/``` -- get list of games with this category
- ```/v1/categories/:id/expansions/``` -- get list of expansions with this category


**Example request:**

    http http://api.meeple.co/v1/categories/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Expansion for Base-game",
        "slug": "expansion-for-base-game",
        "resource_url": "http://api.meeple.co/v1/categories/1/",
        "games": {
            "count": 0,
            "resource_url": "http://api.meeple.co/v1/categories/1/games/"
        },
        "expansions": {
            "count": 8114,
            "resource_url": "http://api.meeple.co/v1/categories/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this category
- ```name``` *string* -- category name
- ```slug``` *string* -- category slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="mechanics"></a>
##Mechanics

All board game mechanics

###Endpoints

- ```/v1/mechanics/``` -- get all mechanics
- ```/v1/mechanics/:id/``` -- get a specific mechanic
- ```/v1/mechanics/:id/games/``` -- get list of games with this mechanic
- ```/v1/mechanics/:id/expansions/``` -- get list of expansions with this mechanic


**Example request:**

    http http://api.meeple.co/v1/mechanic/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Area Control / Area Influence",
        "slug": "area-control-area-influence",
        "resource_url": "http://api.meeple.co/v1/mechanics/1/",
        "games": {
            "count": 1836,
            "resource_url": "http://api.meeple.co/v1/mechanics/1/games/"
        },
        "expansions": {
            "count": 492,
            "resource_url": "http://api.meeple.co/v1/mechanics/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this mechanic
- ```name``` *string* -- mechanic name
- ```slug``` *string* -- mechanic slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="families"></a>
##Families

All board game families

###Endpoints

- ```/v1/families/``` -- get all families
- ```/v1/families/:id/``` -- get a specific family
- ```/v1/families/:id/games/``` -- get list of games with this family
- ```/v1/families/:id/expansions/``` -- get list of expansions with this family


**Example request:**

    http http://api.meeple.co/v1/families/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Promotional Cards",
        "slug": "promotional-cards",
        "resource_url": "http://api.meeple.co/v1/families/1/",
        "games": {
            "count": 0,
            "resource_url": "http://api.meeple.co/v1/families/1/games/"
        },
        "expansions": {
            "count": 173,
            "resource_url": "http://api.meeple.co/v1/families/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this family
- ```name``` *string* -- family name
- ```slug``` *string* -- family slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -

<a name="subdomains"></a>
##Subdomains

All board game subdomains

###Endpoints

- ```/v1/subdomains/``` -- get all subdomains
- ```/v1/subdomains/:id/``` -- get a specific subdomain
- ```/v1/subdomains/:id/games/``` -- get list of games with this subdomain
- ```/v1/subdomains/:id/expansions/``` -- get list of expansions with this subdomain


**Example request:**

    http http://api.meeple.co/v1/subdomains/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "name": "Strategy Games",
        "slug": "strategy-games",
        "resource_url": "http://api.meeple.co/v1/subdomains/1/",
        "games": {
            "count": 1330,
            "resource_url": "http://api.meeple.co/v1/subdomains/1/games/"
        },
        "expansions": {
            "count": 307,
            "resource_url": "http://api.meeple.co/v1/subdomains/1/expanisons/"
        }
    }

**Attributes:**

- ```resource_url``` *string* -- hypermedia URL of this subdomain
- ```name``` *string* -- subdomain name
- ```slug``` *string* -- subdomain slug
- ```games``` *dictonary*
    - ```count``` *int* -- number of games
    - ```resource_url``` *string* -- hypermedia URL to list of games
- ```expanisons``` *dictonary*
    - ```count``` *int* -- number of expanisons
    - ```resource_url``` *string* -- hypermedia URL to list of expanisons

- - -