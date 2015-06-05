# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfred', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybook',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
