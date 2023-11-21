from django.shortcuts import render


# Expected request will carry factory data identifier, and the factory's workstations and sensors
# Create functions to...
# Generate workstationHaltStarts and workstationHaltEnds, then sends these values and the factory data sensors and tasks to the Sensor Data Table within the ddflo DB

# This home page will serve as a spot for the manager / user to generate new information for a selected simulated factory (these are managed in the factory_management_utility app)
def simulated_factory_home(request):
    # return render(request, 'simulated_factory_homepage')
 return render(request, 'simulated.html')


    

def generate_data(request):
    # I'll create a dictionary of scenarios and patterns 
    halt_scenarios = [{'Short' : ''}, {'Medium' : ''}, {'Long' : ''}]
    # I can use a halt count for a workstation, employee combo and use that to determine and map to a reoccurence multiplier
    halt_count = {}
    # Where halt_count retrieves employee id as a key and # halts as the value
    # Map employee id as key to halt occurences
    reoccurence_multiplier = {}
    
    return render(request, "simulated.html")
    
  