# ddflo_sensor_data_utility/urls.py

from django.urls import path
from . import views 
urlpatterns = [
    path('', views.simulated_factory_home, name='simulated_factory_home'),
    # Add other URL patterns as needed
]

