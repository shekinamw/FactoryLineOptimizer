# ddflo_sensor_data_utility/urls.py

from django.urls import path
from . import views 
urlpatterns = [
    path('', views.simulated_factory_home, name='simulated'),
    path('generate_data/', views.generate_data, name='generate_data')
    # Add other URL patterns as needed
]

