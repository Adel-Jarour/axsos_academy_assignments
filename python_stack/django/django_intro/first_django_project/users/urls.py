from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('users/new/', views.register, name='register_alt'),
    path('users/', views.index, name='index'),
]
