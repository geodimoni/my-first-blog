#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 12:08:59 2022

@author: david
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')]
