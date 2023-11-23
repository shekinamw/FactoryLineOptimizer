from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.serializers import serialize
from .models import *
from .forms import FactoryForm
from ddflo_simulated_sensor_data_factory.views import sensor_data_generator
from threading import Thread

# Create your views here.
# In the below context 'pass' allows me to define new functions without code within them, using 'pass' prevents an empty function from throwing an error

# Allow Django to render a dashboard for the factory util
def factory_homepage(request): 
    # Pass a list of factories to the homepage  
    factory = Factory.objects.get(pk=1)
    Thread(target=generator, args=(factory.factory_status,)).start()
    # Need to make this template still
    return render(request, 'factory_homepage.html', {'factory': factory})

def factory_error(request):
    #return render(request, 'factory_error.html')
    pass

# Renders the frontend html template for the user, on this page is the form for registering stations to a specific factory.
def factory_workstation_registration_page(request, factory_identifier):
    # Get a list of premade workstations
    # station_options = Wstations.objects.all()
    # Render these to the page as selection options, can be rendered in the html using for each loop
    # context['stations_options'] = station_options
    #  render(request, 'factory_workstation_registration.html', context)
    pass

# Allows the creation of a new factory
def create_new_factory(request):
    # Ensure the function only proceeds if a post (and no other other HTTP request) was received
    if request.method == 'POST':
        # Get information from the FactoryForm after a POST request is sent to create_new_factory
        form = FactoryForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Save the information provided by the FactoryForm as a record in our Factory Table
            form.save()
            context = {
                'form' : form
            }
            # Render dashboard with new list
        else:
            # Render some kind of error template
            pass

# Allows python to retrieve all the factory records within the ddflo DB, Factory table, only used internally in this views.py file

# Allows python to retreive a single factory record, should we do the query based on name?
# May need to alter this so it works for a search form



# def fetch_all_workstations():
# return Workstation.objects.all().values() 


def fetch_all_wstasks():
    return Wstask.objects.all().values()

def get_random_task():
    return Wstask.objects.order_by('?').first()
    
def fetch_workstation_based_on_task(task_id):
    return Wstask.objects.filter(taskid=task_id).values('workstationid')


def toggle(request):
    toggle_instance = Factory.objects.get(pk=1)
    toggle_instance.factory_status = not toggle_instance.factory_status
    toggle_instance.save()
    # redirect to homepage
    return redirect('factory_homepage')

def generator(toggle):
    sensor_data_generator(toggle, get_random_task())

def fetch_factory_status():
    return Factory.objects.get(pk=1).factory_status
    
