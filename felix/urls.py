# -*- coding: utf-8 -*-
2018 - 10 - 23
__author__ = 'Felix'
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

