from django.shortcuts import render
from django.core.serializers import serialize
from .models import *
from .forms import FactoryForm

# Create your views here.
# In the below context 'pass' allows me to define new functions without code within them, using 'pass' prevents an empty function from throwing an error

# Allow Django to render a dashboard for the factory util
def factory_homepage(request): 
    # Pass a list of factories to the homepage  
    context = fetch_factory_all()

    # Need to make this template still
    return render(request, 'factory_homepage.html', context)

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

# Renders the frontend html template for the user, on this page is the form for creating a new factory --> this form upon submission will send a request to create_new_factory, hanndling the backend logic
def factory_creation_page(request):
    #return render(request, 'factory_creation_page.html')
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
def fetch_factory_all():
    # Fetch all factory records
    factories = Factory.objects.all()
     
     # Serialize the queryset to JSON
     # Serialize the queryset to JSON
    factory_serialized_data = serialize('json', factories, fields=('id', 'factory_type', 'factory_status'))

    return {'factories': factory_serialized_data}

# Allows python to retreive a single factory record, should we do the query based on name?
# May need to alter this so it works for a search form
def fetch_factory_single(factory_identifier):
    # Fetch a single factory record matching the provided factory_identifier
    factory = Factory.objects.get(factory_id = factory_identifier)
    
    # Serialize it
    factory_serialized_data = serialize('json', factory)

    # Convert the serialized data to a native dict
    factory_dict_data = {'factory' : factory_serialized_data}
    
    return factory_dict_data

# Allows python to add map workstations from the ddflo DB, workstations table to the factory -> this should stored in a seperate table (maybe called factory_workstation_associations)
def map_workstations_to_factory():
    # Provide a check for possible conflicting entries (e.g. one factory cannot have multiple of the same workstations?)
    pass

# def fetch_all_workstations():
# return Workstation.objects.all().values() 


def fetch_all_wstasks():
    return Wstask.objects.all().values()

def get_random_task():
    return Wstask.objects.order_by('?').first().taskid
    
# Allows python to delete a factory and it's associated mapped workstations and tasks
def delete_factory_single(request, factory_identifier):
    # Delete factory records where factory_id = factory_identifier
    Factory.objects.filter(factory_id=factory_identifier).delete()
    template_choice = ''

    # We also need to use signal here to ensure the workstations that are associated with the factory are deleted here
    ''' COMPLETE CODE HERE '''
    if Factory.objects.filter(factory_id=factory_identifier).exists():
        template_choice = 'factory_homepage.html'
    else:
        template_choice = 'error_page.html'
    
    return render(request, template_choice)

def fetch_workstation_based_on_task(task_id):
    return Wstask.objects.filter(taskid=task_id).values('workstationid')

def fetch_factory_status(factoryid):
    return 

def alter_factory_status(factoryid):
    if fetch_factory_status(factoryid):
        Factory.objects.filter(factory_id=factoryid).update(factorystatus=False)
    else:
        Factory.objects.filter(factory_id=factoryid).update(factorystatus=True)
        sensor_data_generator(factory_id)
    
