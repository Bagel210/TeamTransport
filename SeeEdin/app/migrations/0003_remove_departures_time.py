# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150220_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departures',
            name='time',
        ),
    ]
