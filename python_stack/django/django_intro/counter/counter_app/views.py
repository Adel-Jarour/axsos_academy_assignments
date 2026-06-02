from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    # Initialize or increment the visit counter
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    
    # Initialize the increment counter if it doesn't exist
    if 'counter_value' not in request.session:
        request.session['counter_value'] = 0
    
    context = {
        'visits': request.session['visits'],
        'counter_value': request.session['counter_value']
    }
    
    return render(request, 'index.html', context)

def destroy_session(request):
    # Clear the session
    request.session.flush()
    # Redirect to root route
    return redirect('/')

def increment_by_two(request):
    # Increment the counter by 2
    if 'counter_value' in request.session:
        request.session['counter_value'] += 2
    else:
        request.session['counter_value'] = 2
    
    return redirect('/')

def increment_by_custom(request):
    if request.method == 'POST':
        # Get the increment value from the form
        increment_value = request.POST.get('increment_value', 1)
        
        try:
            increment_value = int(increment_value)
        except ValueError:
            increment_value = 1
        
        if 'counter_value' in request.session:
            request.session['counter_value'] += increment_value
        else:
            request.session['counter_value'] = increment_value
    
    return redirect('/')