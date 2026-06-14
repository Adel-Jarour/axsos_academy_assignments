from django.shortcuts import get_object_or_404, redirect, render

from shows_app.models import Show

# Create your views here.

def index(request):
    shows = Show.objects.all()
    return render(request, 'index.html', {'shows': shows})

def show(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'show.html', {'show': show})

def create(request):
    if request.method == 'POST':
        show, errors = Show.objects.create_show(request.POST)
        if errors:
            return render(request, 'new_show.html', {'errors': errors, 'data': request.POST})
        return redirect(f'/shows/{show.id}')

    return render(request, 'new_show.html')

def edit(request, id):
    show = get_object_or_404(Show, id=id)

    if request.method == 'POST':
        updated_show, errors = Show.objects.update_show(id, request.POST)
        if errors:
            return render(request, 'edit.html', {'errors': errors, 'show': show, 'data': request.POST})
        return redirect(f'/shows/{updated_show.id}')

    return render(request, 'edit.html', {'show': show})

def destroy(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('/shows')