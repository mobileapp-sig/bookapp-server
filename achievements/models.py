# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group

class Achievement(models.Model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=1024)

class MyAchievement(models.Model):
    user = models.ForeignKey(User)
    achievement = models.ForeignKey(Achievement)
    
