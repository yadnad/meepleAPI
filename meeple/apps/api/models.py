from django.contrib.postgres.fields import ArrayField
from django.db import models

from autoslug import AutoSlugField


class BaseType(models.Model):
    name = models.CharField(max_length=256)
    object_id = models.IntegerField(blank=True, unique=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

    @property
    def games(self):
        return self.game_set.all()

    @property
    def expansions(self):
        return self.expansion_set.all()

    def __unicode__(self):
        return self.name


class Artist(BaseType):
    pass


class Designer(BaseType):
    pass


class Publisher(BaseType):
    pass


class Subdomain(BaseType):
    pass


class Category(BaseType):
    pass


class Mechanic(BaseType):
    pass


class Family(BaseType):
    pass


class Geek(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    num_ratings = models.IntegerField(blank=True, null=True)
    fans = models.IntegerField(blank=True, null=True)
    total_plays = models.IntegerField(blank=True, null=True)
    plays_this_month = models.IntegerField(blank=True, null=True)
    language_dependence = models.CharField(max_length=250, blank=True, null=True)

    suggested_age = models.IntegerField(blank=True, null=True)

    users_owning = models.IntegerField(blank=True, null=True)
    users_trading = models.IntegerField(blank=True, null=True)
    users_wanting = models.IntegerField(blank=True, null=True)

    object_id = models.IntegerField(unique=True)

    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def rank(self):
        return self.rank_set.all()

    @property
    def suggested_players(self):
        return self.geekplayers_set.all()

    def __unicode__(self):
        return u'{0}'.format(self.object_id)


class GameBase(models.Model):
    name = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='name', unique=True)
    age = models.IntegerField(blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    playing_time = models.IntegerField(blank=True, null=True)

    max_players = models.IntegerField(blank=True, null=True)
    min_players = models.IntegerField(blank=True, null=True)

    artists = models.ManyToManyField('Artist')
    designers = models.ManyToManyField('Designer')
    publishers = models.ManyToManyField('Publisher')
    mechanics = models.ManyToManyField('Mechanic')
    categories = models.ManyToManyField('Category')
    subdomains = models.ManyToManyField('Subdomain')
    families = models.ManyToManyField('Family')

    image = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    geek = models.OneToOneField('Geek', blank=True, null=True)

    @property
    def players(self):
        if self.min_players == self.max_players:
            return self.min_players
        else:
            return '{0} - {1}'.format(self.min_players, self.max_players)

    class Meta:
        abstract = True


class Game(GameBase):
    expansions = models.ManyToManyField('Expansion')
    integrations = models.ManyToManyField('Game')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('geek__ranking',)


class Expansion(GameBase):
    @property
    def games(self):
        return self.game_set.all()

    def __unicode__(self):
        return self.name


class Rank(models.Model):
    geek = models.ForeignKey("Geek", null=True, blank=True)
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')
    rank = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.name, self.rank)


class GeekPlayers(models.Model):
    geek = models.ForeignKey("Geek", null=True, blank=True)
    recommended = ArrayField(models.CharField(max_length=3), default=[], blank=True)
    not_recommended = ArrayField(models.CharField(max_length=3), default=[], blank=True)
    best = ArrayField(models.CharField(max_length=3), default=[], blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.id)

