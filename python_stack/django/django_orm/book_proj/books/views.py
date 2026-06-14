from django.shortcuts import render, redirect, get_object_or_404
from books.models import User, Book


# ─── Helpers ────────────────────────────────────────────────────────────────

def get_logged_in_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


# ─── Auth views ─────────────────────────────────────────────────────────────

def index(request):
    if get_logged_in_user(request):
        return redirect('books_index')
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user, errors = User.objects.register_user(request.POST)
        if errors:
            return render(request, 'index.html', {
                'register_errors': errors,
                'register_data': request.POST,
            })
        request.session['user_id'] = user.id
        return redirect('books_index')
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        user, errors = User.objects.login_user(request.POST)
        if errors:
            return render(request, 'index.html', {
                'login_errors': errors,
                'login_data': request.POST,
            })
        request.session['user_id'] = user.id
        return redirect('books_index')
    return redirect('index')


def logout_view(request):
    request.session.flush()
    return redirect('index')


# ─── Books views ─────────────────────────────────────────────────────────────

def books_index(request):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book_errors = request.session.pop('book_errors', {})
    book_data = request.session.pop('book_data', {})

    all_books = Book.objects.select_related('uploaded_by').prefetch_related('users_who_like').all()
    liked_ids = set(user.liked_books.values_list('id', flat=True))

    return render(request, 'books.html', {
        'user': user,
        'all_books': all_books,
        'liked_ids': liked_ids,
        'book_errors': book_errors,
        'book_data': book_data,
    })


def add_book(request):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        errors = {}

        if not title:
            errors['title'] = 'Title is required.'
        if len(desc) < 5:
            errors['desc'] = 'Description must be at least 5 characters.'

        if errors:
            request.session['book_errors'] = errors
            request.session['book_data'] = {'title': title, 'desc': desc}
            return redirect('books_index')

        book = Book.objects.create(
            title=title,
            desc=desc,
            uploaded_by=user,
        )
        # Auto-favorite by uploader
        book.users_who_like.add(user)
        return redirect('books_index')

    return redirect('books_index')


def book_detail(request, id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book = get_object_or_404(Book, id=id)
    is_uploader = (book.uploaded_by == user)
    has_favorited = book.users_who_like.filter(id=user.id).exists()
    likers = book.users_who_like.all()

    update_errors = request.session.pop('update_errors', {})

    return render(request, 'book_detail.html', {
        'user': user,
        'book': book,
        'is_uploader': is_uploader,
        'has_favorited': has_favorited,
        'likers': likers,
        'update_errors': update_errors,
    })


def update_book(request, id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book = get_object_or_404(Book, id=id)

    if book.uploaded_by != user:
        return redirect('book_detail', id=id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        desc = request.POST.get('desc', '').strip()
        errors = {}

        if not title:
            errors['title'] = 'Title is required.'
        if len(desc) < 5:
            errors['desc'] = 'Description must be at least 5 characters.'

        if errors:
            request.session['update_errors'] = errors
            return redirect('book_detail', id=id)

        book.title = title
        book.desc = desc
        book.save()
        return redirect('book_detail', id=id)

    return redirect('book_detail', id=id)


def delete_book(request, id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book = get_object_or_404(Book, id=id)
    if book.uploaded_by == user:
        book.delete()
    return redirect('books_index')


def favorite_book(request, id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book = get_object_or_404(Book, id=id)
    book.users_who_like.add(user)

    # Return to wherever the user came from
    referer = request.META.get('HTTP_REFERER', '')
    if f'/books/{id}/' in referer:
        return redirect('book_detail', id=id)
    return redirect('books_index')


def unfavorite_book(request, id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('index')

    book = get_object_or_404(Book, id=id)
    book.users_who_like.remove(user)

    referer = request.META.get('HTTP_REFERER', '')
    if f'/books/{id}/' in referer:
        return redirect('book_detail', id=id)
    return redirect('books_index')
