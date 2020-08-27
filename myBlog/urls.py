#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'myBlog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
]
