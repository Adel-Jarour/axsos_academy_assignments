# blogs/views.py
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

# / - redirects to "/blogs"
def root(request):
    return redirect('/blogs')

# /blogs - display list placeholder
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# /blogs/new - display new form placeholder
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# /blogs/create - redirect to "/"
def create(request):
    return redirect('/')

# /blogs/<number> - display blog number
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# /blogs/<number>/edit - display edit placeholder
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# /blogs/<number>/delete - redirect to "/blogs"
def destroy(request, number):
    return redirect('/blogs')

# BONUS: /blogs/json - return JSON response
def json_response(request):
    data = {
        "title": "My first blog",
        "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
    }
    return JsonResponse(data)