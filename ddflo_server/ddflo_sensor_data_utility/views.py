from django.shortcuts import render
from ddflo_sensor_data_utility.models import *
from datetime import date

# Create your views here.

def sensor_data_util_home(request):
    
    # Fetch a list of all sensors
    # render(request, 'sensor_data_home.html', )
    pass

# Creat a sensor data, used for the generator
def create_sensor_record(halt_start, halt_end, task):
    Sensordata.objects.create(haltstart=halt_start, haltend=halt_end, taskid = task)

def sensor_data_logs(request):
    # Fetch all records from today  
    present_day = date.today()
    sensor_data_logs = Sensordata.objects.filter(haltstart__date=present_day)

    # Format as dict
    context = {}
    context['sensor_data_logs'] = sensor_data_logs

    # Return page
    render(request, 'sensor_data_logging.html' , context)
