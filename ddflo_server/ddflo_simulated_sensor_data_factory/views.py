from datetime import datetime
from django.shortcuts import render, redirect

from ddflo_sensor_data_utility.views import create_sensor_record
from random import randint
import time

# Expected request will carry factory data identifier, and the factory's workstations and sensors
# Create functions to...
# Generate workstationHaltStarts and workstationHaltEnds, then sends these values and the factory data sensors and tasks to the Sensor Data Table within the ddflo DB

# This home page will serve as a spot for the manager / user to generate new information for a selected simulated factory (these are managed in the factory_management_utility app)
def simulated_factory_home(request):
    return render(request, 'simulated-factory-home.html')
    
def generate_one_halt_event(task):
    duration = randint(10, 100)
    halt_start = datetime.now()
    time.sleep(duration)
    halt_end = datetime.now()
    create_sensor_record(halt_start, halt_end, task)


# Takes in a boolean value, 
def sensor_data_generator(status, task): # runs the loop, continues untill the factory is turned off
    while status:
        delay = randint(100, 3600)
        time.sleep(delay)
        if status:
            break
        generate_one_halt_event(task)