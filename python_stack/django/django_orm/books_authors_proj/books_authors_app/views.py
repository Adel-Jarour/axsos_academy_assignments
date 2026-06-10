from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def books(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        if title:
            Book.objects.create(title=title, desc=desc)
    return redirect('/')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    associated_authors = book.author.all()
    # SENSEI BONUS: Dropdown list excludes already associated authors
    remaining_authors = Author.objects.exclude(id__in=associated_authors.values_list('id', flat=True))
    context = {
        'book': book,
        'associated_authors': associated_authors,
        'remaining_authors': remaining_authors
    }
    return render(request, 'book_detail.html', context)

def add_author_to_book(request, book_id):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        if author_id:
            book = Book.objects.get(id=book_id)
            author = Author.objects.get(id=author_id)
            book.author.add(author)
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        if first_name and last_name:
            Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    associated_books = author.books.all()
    # SENSEI BONUS: Dropdown list excludes already associated books
    remaining_books = Book.objects.exclude(id__in=associated_books.values_list('id', flat=True))
    context = {
        'author': author,
        'associated_books': associated_books,
        'remaining_books': remaining_books
    }
    return render(request, 'author_detail.html', context)

def add_book_to_author(request, author_id):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            author = Author.objects.get(id=author_id)
            book = Book.objects.get(id=book_id)
            author.books.add(book)
    return redirect(f'/authors/{author_id}')

