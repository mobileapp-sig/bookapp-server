# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from books.models import Book

class MyBook(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    rating = models.SmallIntegerField(default=0)

class Checkpoint(models.Model):
    PURCHASE = 'P'
    BORROW = 'B'
    RETURN = 'R'
    START_BOOK = 'S'
    END_BOOK = 'E'
    START_READ = 's'
    PAUSE_READ = 'p'
    RESUME_READ = 'r'
    END_READ = 'e'
    BOOKMARK = 'm'
    MEMO = 'M'

    CHECKPOINT_TYPES = (
        (PURCHASE, 'Purchase'),
        (BORROW, 'Borrow'),
        (RETURN, 'Return'),
        (START_BOOK, 'Start Book'),
        (END_BOOK, 'End Book'),
        (START_READ, 'Start Read'),
        (PAUSE_READ, 'Pause Read'),
        (RESUME_READ, 'Resume Read'),
        (END_READ, 'End Read'),
        (BOOKMARK, 'Bookmark'),
        (MEMO, 'Memo'),
    )

    mybook = models.ForeignKey(MyBook)
    timestamp = models.DateTimeField(auto_now_add=True)
    cptype = models.CharField(max_length=1, choices=CHECKPOINT_TYPES)
    page = models.SmallIntegerField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

class WishList(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

