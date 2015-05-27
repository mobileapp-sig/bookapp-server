# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
