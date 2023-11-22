from django.shortcuts import render
from ddflo_factory_management_utility.models import Workstation

#new stuff
# Create your views here.
def home(request):
    return render(request, "Homepage.html")