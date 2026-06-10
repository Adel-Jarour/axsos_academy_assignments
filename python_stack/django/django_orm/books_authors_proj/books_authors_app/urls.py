from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('books/add', views.add_book, name='add_book'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/add_author', views.add_author_to_book, name='add_author_to_book'),
    path('authors', views.authors, name='authors'),
    path('authors/add', views.add_author, name='add_author'),
    path('authors/<int:author_id>', views.author_detail, name='author_detail'),
    path('authors/<int:author_id>/add_book', views.add_book_to_author, name='add_book_to_author'),
]