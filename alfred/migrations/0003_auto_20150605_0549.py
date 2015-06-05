# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfred', '0002_auto_20150605_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpoint',
            name='page',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
