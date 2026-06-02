from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from datetime import datetime

def index(request):
    # Initialize session variables if they don't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    # Define the activities list
    activities_list = [
        {'name': 'Farm', 'description': '(earns 10-20 gold)', 'location': 'farm', 'min': 10, 'max': 20},
        {'name': 'Cave', 'description': '(earns 10-20 gold)', 'location': 'cave', 'min': 10, 'max': 20},
        {'name': 'House', 'description': '(earns 10-20 gold)', 'location': 'house', 'min': 10, 'max': 20},
        {'name': 'Quest', 'description': '(earns/takes 0-50 gold)', 'location': 'quest', 'min': -50, 'max': 50},
    ]

    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities'],
        'activities_list': activities_list,
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        
        # Determine gold earned/lost based on location
        if location == 'farm':
            gold_earned = random.randint(10, 20)
            message = f"You entered a farm and earned {gold_earned} gold."
            color = 'green'
            
        elif location == 'cave':
            gold_earned = random.randint(10, 20)
            message = f"You entered a cave and earned {gold_earned} gold."
            color = 'green'
            
        elif location == 'house':
            gold_earned = random.randint(10, 20)
            message = f"You entered a house and earned {gold_earned} gold."
            color = 'green'
            
        elif location == 'quest':
            gold_earned = random.randint(-50, 50)
            if gold_earned >= 0:
                message = f"You completed a quest and earned {gold_earned} gold."
                color = 'green'
            else:
                message = f"You failed a quest and lost {abs(gold_earned)} gold. Ouch."
                color = 'red'
        else:
            gold_earned = 0
            message = "Invalid location."
            color = 'black'
        
        # Update gold
        request.session['gold'] = request.session.get('gold', 0) + gold_earned
        
        # Add activity to log with timestamp
        timestamp = datetime.now().strftime("%B %dth %Y %I:%M %p")
        activity = {
            'message': message,
            'color': color,
            'timestamp': timestamp
        }
        
        activities = request.session.get('activities', [])
        activities.insert(0, activity)  # Newest activities at the top
        request.session['activities'] = activities[:20]  # Keep only last 20 activities
        
        request.session.modified = True
        
    return redirect('index')

def reset(request):
    # Clear session to reset the game
    request.session.flush()
    return redirect('index')