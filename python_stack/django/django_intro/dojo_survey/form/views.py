# form/views.py (Enhanced version)
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    """Display the form page"""
    return render(request, 'index.html')

def result(request):
    """Process the form and display results"""
    
    # Get form data from POST request
    context = {
        'name': request.POST.get('name', 'Not provided'),
        'email': request.POST.get('email', 'Not provided'),
        'age': request.POST.get('age', 'Not provided'),
        'gender': request.POST.get('gender', 'Not provided'),
        'interest': request.POST.getlist('interest'),  # For multiple checkboxes
        'newsletter': request.POST.get('newsletter', 'off'),
        'comments': request.POST.get('comments', 'No comments provided'),
        'favorite_color': request.POST.get('favorite_color', 'Not selected'),
    }
    
    return render(request, 'result.html', context)