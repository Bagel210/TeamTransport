# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('stop_name', models.CharField(max_length=200)),
                ('departures', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departures',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('valid_from', models.IntegerField()),
                ('day', models.IntegerField(max_length=1)),
                ('time', models.TimeField()),
                ('service_name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='attraction',
            old_name='name',
            new_name='attraction_name',
        ),
        migrations.AddField(
            model_name='attraction',
            name='bus_stop',
            field=models.ForeignKey(related_name='closest_stop', to='app.BusStop', default=0),
            preserve_default=False,
        ),
    ]
