from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<int:course_id>/destroy/', views.destroy, name='destroy'),
    path('courses/<int:course_id>/comments/', views.comments, name='comments'),
]
