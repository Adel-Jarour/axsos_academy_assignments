from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# /surveys - display all the surveys created
def index(request):
    return HttpResponse("placeholder to display all the surveys created.")

# /surveys/new - display form to add new survey
def new(request):
    return HttpResponse("placeholder for users to add a new survey.")
