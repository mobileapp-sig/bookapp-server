# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20150527_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cptype', models.CharField(max_length=1, choices=[(b'P', b'Purchase'), (b'B', b'Borrow'), (b'R', b'Return'), (b'S', b'Start Book'), (b'E', b'End Book'), (b's', b'Start Read'), (b'p', b'Pause Read'), (b'r', b'Resume Read'), (b'e', b'End Read'), (b'm', b'Bookmark'), (b'M', b'Memo')])),
                ('page', models.SmallIntegerField()),
                ('memo', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.SmallIntegerField()),
                ('book', models.ForeignKey(to='books.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.ForeignKey(to='books.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='mybook',
            field=models.ForeignKey(to='alfred.MyBook'),
        ),
    ]
