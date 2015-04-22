# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150411_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expansion',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
