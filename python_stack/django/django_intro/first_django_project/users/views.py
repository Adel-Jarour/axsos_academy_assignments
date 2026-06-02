from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# /register & /users/new - create new user record placeholder
def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

# /login - login placeholder
def login(request):
    return HttpResponse("placeholder for users to log in.")

# /users - display list of users placeholder
def index(request):
    return HttpResponse("placeholder to display all the list of users later.")
