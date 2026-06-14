from django.urls import path

from shows_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),        # GET = form, POST = submit
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit/', views.edit, name='edit'),  # GET = form, POST = update
    path('<int:id>/destroy/', views.destroy, name='destroy'),
]