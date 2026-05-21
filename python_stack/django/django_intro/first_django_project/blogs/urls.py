# blogs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /blogs - display all blogs
    path('', views.index, name='index'),
    
    # /blogs/new - display new form
    path('new/', views.new, name='new'),
    
    # /blogs/create - create new blog (redirects to /)
    path('create/', views.create, name='create'),
    
    # /blogs/<number> - show specific blog
    path('<int:number>/', views.show, name='show'),
    
    # /blogs/<number>/edit - edit specific blog
    path('<int:number>/edit/', views.edit, name='edit'),
    
    # /blogs/<number>/delete - delete specific blog
    path('<int:number>/delete/', views.destroy, name='destroy'),
    
    # BONUS: /blogs/json - return JSON
    path('json/', views.json_response, name='json'),
]