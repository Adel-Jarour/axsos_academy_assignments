# form/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      # Root route - shows form
    path('result/', views.result, name='result'),  # Result route - shows submitted data
]