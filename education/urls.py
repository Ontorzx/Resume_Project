from django.contrib import admin
from django.urls import path
from education import views
urlpatterns = [
    path('skill',views.Skill,name='skill'),
]