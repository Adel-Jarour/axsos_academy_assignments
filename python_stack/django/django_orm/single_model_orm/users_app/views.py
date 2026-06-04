from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
# Create your views here.

def index(request):
    context = {
        "users": models.User.objects.all()
    }
    return render(request, "index.html", context)

def add_user(request):
    if request.method == "POST":
        email = request.POST["email_address"]
        if models.User.objects.filter(email_address=email).exists():
            messages.error(request, "A user with this email address already exists.")
            return redirect("/")
            
        models.User.objects.create(
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"],
            email_address = email,
            age = request.POST["age"]
        )
        return redirect("/")