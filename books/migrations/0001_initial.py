# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_isbn', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200, blank=True)),
                ('publisher', models.CharField(max_length=200, blank=True)),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('pubdate', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_rating', models.SmallIntegerField()),
                ('book', models.ForeignKey(to='books.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
