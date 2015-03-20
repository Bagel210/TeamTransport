# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_departures_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=20)),
                ('atco_code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('orientation', models.IntegerField()),
                ('direction', models.CharField(max_length=2)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
