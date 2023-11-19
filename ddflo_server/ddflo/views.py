from django.shortcuts import render
from .models import Workstation

#new stuff
# Create your views here.
def home(request):
    return render(request, "Homepage.html")