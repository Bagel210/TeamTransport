# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='bus_stop',
            field=models.ForeignKey(related_name='closest_stop', to='app.Stops'),
            preserve_default=True,
        ),
    ]
