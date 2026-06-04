from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user', views.add_user, name='add_user'),
]
