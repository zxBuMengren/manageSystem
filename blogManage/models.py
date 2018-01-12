# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)
    content =models.TextField(max_length=10000)

admin.site.register(article)

class user(models.Model):
    useraccount = models.CharField(max_length=40,null=False,blank=False)
    username = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    birth = models.DateField(auto_now=False,auto_now_add=False)
    password = models.CharField(max_length=50,null=False,blank=False)

admin.site.register(user)