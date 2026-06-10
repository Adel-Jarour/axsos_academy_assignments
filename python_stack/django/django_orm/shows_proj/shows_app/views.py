from django.shortcuts import redirect, render

from shows_app.models import Show

# Create your views here.

def index(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'index.html', context)

def newShow(request):
    return render(request, 'new_show.html')

def create(request):
    if request.method == 'POST':
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect(f'/shows/{show.id}')
    return redirect('/shows')

def show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'show.html', context)

def edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'edit.html', context)

def update(request, id):
    if request.method == 'POST':
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect('/shows')

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')