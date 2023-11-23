from django.urls import path
from ddflo_simulated_sensor_data_factory import views

urlpatterns = [
    path('', views.simulated_factory_home, name="simulated-factory-home"),
]