from django.urls import path, include
from . import views

urlpatterns = [
    path("factory_homepage", views.factory_homepage, name="factory_homepage"),
  path('delete_factory/<int:factory_id>/', views.delete_factory, name='delete_factory'),
  path('create-new-factory/', views.create_new_factory, name='create_new_factory'),
  path('factory/<int:factory_identifier>/register_workstation/', views.register_workstation, name='register_workstation'),


    # Define the URL for the registration view (where the form is submitted)
    path('factory/register_workstation/', views.register_workstation, name='register_workstation'),
]