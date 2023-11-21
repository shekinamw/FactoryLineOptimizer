# ddflo/views.py
# ddflo/views.py
from django.shortcuts import render
#from django.http import HttpResponse

from .models import  Schedule 

def schedule_list(request):
    context = {}
    all_schedules = Schedule.objects.all()
    context['schedules'] = all_schedules
    return render(request, 'schedule.html', context)


def home(request):
     return render (request, "base.html")


def calendar_view(request):
    # Your existing calendar view logic
    # ...
    return render(request, 'ddflo/calendar_view.html')

