from django.shortcuts import render
from .models import Workstation

#new stuff
# Create your views here.
def home(request):
    # Workstation.objects.create(workstationid=7654321, workstationname='Junk Data, remove')
    raw_vals = Workstation.objects.filter(workstationid=654321).values()
    get_that_data = {'workstationid' : [], 'workstationname' : []}
    for x in raw_vals:
        get_that_data['workstationid'].append(x['workstationid'])
        get_that_data['workstationname'].append(x['workstationname'])
    return render(request, "Homepage.html", get_that_data)