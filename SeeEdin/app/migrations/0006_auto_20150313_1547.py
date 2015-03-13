# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_stops_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='stops',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stops',
            name='stop_id',
            field=models.CharField(max_length=20),
        ),
    ]
