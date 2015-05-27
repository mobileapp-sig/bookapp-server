from django.db import models
from django.contrib.auth.models import User, Group

class Book(models.Model):
    _isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    pubdate = models.DateField(blank=True)

class BookRating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    _rating = models.SmallIntegerField()
    
