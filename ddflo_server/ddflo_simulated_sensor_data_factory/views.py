from datetime import datetime
from django.shortcuts import render, redirect
from ddflo_factory_management_utility.views import fetch_factory_status
from ddflo_sensor_data_utility.views import *

# Expected request will carry factory data identifier, and the factory's workstations and sensors
# Create functions to...
# Generate workstationHaltStarts and workstationHaltEnds, then sends these values and the factory data sensors and tasks to the Sensor Data Table within the ddflo DB

# This home page will serve as a spot for the manager / user to generate new information for a selected simulated factory (these are managed in the factory_management_utility app)
def simulated_factory_home(request):
    return render(request, 'simulated-factory-home.html')
    
def generate_one_halt_event():
    duration = randint(10, 100)
    halt_start = datetime.now()
    delay(duration)
    halt_end = datetime.now()
    taskid = get_random_task()
    create_sensor_record(halt_start, halt_end, taskid)


# Takes in a boolean value, 
def sensor_data_generator(factory_id): # runs the loop, continues untill the factory is turned off
    while fetch_factory_status(factory_id):
        delay = randint(100, 3600)
        sleep(delay)
        if fetch_factory_status(factory_id):
            break
        generate_one_halt_event()