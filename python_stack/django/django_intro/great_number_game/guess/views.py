from django.shortcuts import render, redirect
import random

def index(request):
    # Initialize the game if it's a new session
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    
    # Get the result from session or set to None
    result = request.session.get('result')
    
    context = {
        'result': result,  # Make sure this is passed
        'random_number': request.session.get('random_number'),
        'attempts': request.session.get('attempts', 0),
    }
    
    return render(request, 'index.html', context)

def guess(request):
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        random_number = request.session.get('random_number')
        attempts = request.session.get('attempts', 0)
        
        # Increment attempts
        attempts += 1
        request.session['attempts'] = attempts
        
        # Check the guess and store result in session
        if guess == random_number:
            request.session['result'] = 'correct'
        elif guess < random_number:
            request.session['result'] = 'too_low'
        else:
            request.session['result'] = 'too_high'
    
    return redirect('/')

def reset(request):
    # Clear the session and start a new game
    request.session.flush()
    return redirect('/')