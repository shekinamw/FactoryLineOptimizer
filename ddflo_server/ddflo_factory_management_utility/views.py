from django.shortcuts import render,get_object_or_404, redirect
from django.core.serializers import serialize
from .models import Factory,Wstations
from .forms import FactoryForm
from django.http import HttpResponseNotFound

# Create your views here.
# In the below context 'pass' allows me to define new functions without code within them, using 'pass' prevents an empty function from throwing an error

# Allow Django to render a dashboard for the factory util
def factory_homepage(request):
    # Create a sample list of factory objects for testing
    sample_factories = [
        Factory(factory_id=1, factory_location='Location 1', factory_type=Factory.REAL),
        Factory(factory_id=2, factory_location='Location 2', factory_type=Factory.SIMULATED),
        # Add more sample factories as needed
    ]

    # Render the template with the sample factories
    return render(request, 'factory_homepage.html', {'factories': sample_factories})

#def factory_homepage(request):
    #factories = Factory.objects.all()
    #return render(request, 'factory_homepage.html', {'factories': factories})
    

def factory_error(request):
    #return render(request, 'factory_error.html')
    pass

# Renders the frontend html template for the user, on this page is the form for registering stations to a specific factory.
#def factory_workstation_registration_page(request, factory_identifier):
    # Get a list of premade workstations
    # station_options = Wstations.objects.all()
    # Render these to the page as selection options, can be rendered in the html using for each loop
    # context['stations_options'] = station_options
    #  render(request, 'factory_workstation_registration.html', context)
    #pass
def factory_workstation_registration_page(request, factory_identifier):
    # Get a list of premade workstations
    station_options = Wstations.objects.all()
    context = {
        'station_options': station_options,
        'factory_identifier': factory_identifier,
    }
    return render(request, 'factory_workstation_registration.html', context)

# views.py

def register_workstation(request, factory_identifier):
    # Your view logic here
    # ...

    return render(request, 'factory_workstation_registration.html', {'factory_identifier': factory_identifier})

# Renders the frontend html template for the user, on this page is the form for creating a new factory --> this form upon submission will send a request to create_new_factory, hanndling the backend logic
def factory_creation_page(request):
    #return render(request, 'factory_creation_page.html')
    pass

# Allows the creation of a new factory
def create_new_factory(request):
    if request.method == 'POST':
        form = FactoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Render success template or redirect to success page
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'error.html', {'error_message': error_message})
        else:
            error_message = "Invalid form data. Please check your input."
            return render(request, 'error.html', {'error_message': error_message})
    else:
        # Render the form for GET requests
        form = FactoryForm()
        return render(request, 'create_new_factory.html', {'form': form})
# Allows python to retrieve all the factory records within the ddflo DB, Factory table, only used internally in this views.py file
def fetch_factory_all():
    # Fetch all factory records
    factories = Factory.objects.all()
     
     # Serialize the queryset to JSON
    factory_serialized_data = serialize('json', factories)

    # Convert the serialized data to a native Dictionary
    factory_dict_data = {'factories': factory_serialized_data}

    return factory_dict_data

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

# Allows python to alter a specific factory record, this will need special attention in regards to the effect for the workstations and tasks associated with this factory   
def alter_factory_single(request):


    # Check what field is being altered? Or just overwrite every field by default?
    # render failure -> go to errors template, pass error info to the html template
    # render success -> go back to homepage
    pass

# Allows python to add map workstations from the ddflo DB, workstations table to the factory -> this should stored in a seperate table (maybe called factory_workstation_associations)
def map_workstations_to_factory():
    # Provide a check for possible conflicting entries (e.g. one factory cannot have multiple of the same workstations?)
    pass

# Allows python to delete a factory and it's associated mapped workstations and tasks
#def delete_factory_single(request, factory_identifier):
    # Delete factory records where factory_id = factory_identifier
   # Factory.objects.filter(factory_id=factory_identifier).delete()
    #template_choice = ''
def delete_factory(request, factory_id):
    try:
        factory = get_object_or_404(Factory, id=factory_id)
        factory.delete()
        return redirect('factory_homepage')
    except Factory.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Factory not found'})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})
    ''' COMPLETE CODE HERE '''
    if Factory.objects.filter(factory_id=factory_identifier).exists():
        template_choice = 'factory_homepage.html'
    else:
        template_choice = 'error_page.html'
    
    return render(request, template_choice)
