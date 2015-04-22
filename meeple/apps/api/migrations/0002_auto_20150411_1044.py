# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expansion',
            name='language_dependence',
        ),
        migrations.RemoveField(
            model_name='game',
            name='language_dependence',
        ),
        migrations.AddField(
            model_name='geek',
            name='language_dependence',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
