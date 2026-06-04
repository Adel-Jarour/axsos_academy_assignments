from django.shortcuts import render, redirect
from .models import Dojo, Ninja
# Create your views here.

def index(request):
    dojos = Dojo.objects.all()
    context = {
        "dojos": dojos,
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            state=request.POST["state"]
        )
    return redirect("/")

def add_ninja(request):
    if request.method == "POST":
        dojo_id = request.POST["dojo"]
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            dojo=dojo
        )
    return redirect("/")

