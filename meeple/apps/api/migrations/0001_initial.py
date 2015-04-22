# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('age', models.IntegerField(blank=True)),
                ('year_published', models.IntegerField(null=True, blank=True)),
                ('playing_time', models.IntegerField(null=True, blank=True)),
                ('language_dependence', models.CharField(max_length=250, null=True, blank=True)),
                ('max_players', models.IntegerField(null=True, blank=True)),
                ('min_players', models.IntegerField(null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('thumbnail', models.URLField(null=True, blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('artists', models.ManyToManyField(to='api.Artist')),
                ('categories', models.ManyToManyField(to='api.Category')),
                ('designers', models.ManyToManyField(to='api.Designer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('age', models.IntegerField(blank=True)),
                ('year_published', models.IntegerField(null=True, blank=True)),
                ('playing_time', models.IntegerField(null=True, blank=True)),
                ('language_dependence', models.CharField(max_length=250, null=True, blank=True)),
                ('max_players', models.IntegerField(null=True, blank=True)),
                ('min_players', models.IntegerField(null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('thumbnail', models.URLField(null=True, blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('artists', models.ManyToManyField(to='api.Artist')),
                ('categories', models.ManyToManyField(to='api.Category')),
                ('designers', models.ManyToManyField(to='api.Designer')),
                ('expansions', models.ManyToManyField(to='api.Expansion')),
                ('families', models.ManyToManyField(to='api.Family')),
            ],
            options={
                'ordering': ('geek__ranking',),
            },
        ),
        migrations.CreateModel(
            name='Geek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ranking', models.IntegerField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('average_rating', models.FloatField(null=True, blank=True)),
                ('num_ratings', models.IntegerField(null=True, blank=True)),
                ('fans', models.IntegerField(null=True, blank=True)),
                ('total_plays', models.IntegerField(null=True, blank=True)),
                ('plays_this_month', models.IntegerField(null=True, blank=True)),
                ('suggested_age', models.IntegerField(null=True, blank=True)),
                ('users_owning', models.IntegerField(null=True, blank=True)),
                ('users_trading', models.IntegerField(null=True, blank=True)),
                ('users_wanting', models.IntegerField(null=True, blank=True)),
                ('object_id', models.IntegerField(unique=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeekPlayers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommended', django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(max_length=3), blank=True)),
                ('not_recommended', django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(max_length=3), blank=True)),
                ('best', django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(max_length=3), blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('geek', models.ForeignKey(blank=True, to='api.Geek', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('rank', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('geek', models.ForeignKey(blank=True, to='api.Geek', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('object_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='geek',
            field=models.OneToOneField(null=True, blank=True, to='api.Geek'),
        ),
        migrations.AddField(
            model_name='game',
            name='integrations',
            field=models.ManyToManyField(to='api.Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='mechanics',
            field=models.ManyToManyField(to='api.Mechanic'),
        ),
        migrations.AddField(
            model_name='game',
            name='publishers',
            field=models.ManyToManyField(to='api.Publisher'),
        ),
        migrations.AddField(
            model_name='game',
            name='subdomains',
            field=models.ManyToManyField(to='api.Subdomain'),
        ),
        migrations.AddField(
            model_name='expansion',
            name='families',
            field=models.ManyToManyField(to='api.Family'),
        ),
        migrations.AddField(
            model_name='expansion',
            name='geek',
            field=models.OneToOneField(null=True, blank=True, to='api.Geek'),
        ),
        migrations.AddField(
            model_name='expansion',
            name='mechanics',
            field=models.ManyToManyField(to='api.Mechanic'),
        ),
        migrations.AddField(
            model_name='expansion',
            name='publishers',
            field=models.ManyToManyField(to='api.Publisher'),
        ),
        migrations.AddField(
            model_name='expansion',
            name='subdomains',
            field=models.ManyToManyField(to='api.Subdomain'),
        ),
    ]
