from django.shortcuts import render, redirect

from auth_app.models import User

# Create your views here.

def index(request):
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
        return redirect('/success/')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        user, errors = User.objects.login_user(request.POST)
        if errors:
            return render(request, 'index.html', {
                'login_errors': errors,
                'login_data': request.POST,
            })
        request.session['user_id'] = user.id
        return redirect('/success/')
    return render(request, 'index.html')

def success(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/')
    user = User.objects.get(id=user_id)
    return render(request, 'success.html', {'user': user})

def logout(request):
    request.session.flush()   # clears all session data
    return redirect('/')