# time_display/views.py
from django.shortcuts import render
from time import gmtime, strftime  # As shown in the assignment image
import datetime

def index(request):
    # Using the exact method shown in the assignment
    
    now = datetime.datetime.now()

    context = {
        "time": now.strftime("%Y-%m-%d %I:%M %p"),  # Format: 2026-05-20 12:50 PM
        "date": now.strftime("%Y-%m-%d"),
        "time_12hr": now.strftime("%I:%M %p"),
    }
    return render(request, 'index.html', context)