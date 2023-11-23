# ddflo/views.py
# ddflo/views.py
from django.shortcuts import render
from ddflo_factory_management_utility.models import Workstation

def home(request):
     return render (request, "base.html")

