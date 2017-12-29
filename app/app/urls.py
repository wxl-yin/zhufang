"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from room import views as room_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^room/index/$',room_views.index),
    url(r'^room/add/$',room_views.add,name='add'),
    url(r'^room/add2/(\d+)/(\d+)/$',room_views.old_add_redirect_new_add),
    url(r'^room/add2_(\d+)_(\d+)/$',room_views.add2,name='add2'),
]
