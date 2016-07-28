# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search$', views.new, name='home'),
    url(r'^new$', views.new, name='new'),
]