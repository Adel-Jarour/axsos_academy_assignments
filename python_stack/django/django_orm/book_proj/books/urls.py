from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Books
    path('books/', views.books_index, name='books_index'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/update/', views.update_book, name='update_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),
    path('books/<int:id>/favorite/', views.favorite_book, name='favorite_book'),
    path('books/<int:id>/unfavorite/', views.unfavorite_book, name='unfavorite_book'),
]