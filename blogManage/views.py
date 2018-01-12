# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blogManage.models import article
# Create your views here.

def showArticle(request):
    blog = article.objects.order_by('id')
    return render(request,'index.html',{'blog':blog})