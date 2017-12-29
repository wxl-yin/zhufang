# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# 跳转
from django.http import HttpResponseRedirect
# 根据名称获取链接地址
from django.core.urlresolvers import reverse
# Create your views here.

# 首页
def index(request):
    string = u'这个是我需要渲染到页面的数据'
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request,'room/index.html',{'string':string,'list':list,'dic':info_dict})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(int(c))

# 老链接地址
def old_add_redirect_new_add(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )

# 新链接地址
def add2(request,a,b):
    # a = request.GET['a']
    # b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(int(c))