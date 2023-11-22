from django.urls import path
from . import views

urlpatterns = [
   path("", views.factory_homepage, name="factory_homepage"),
   path("alter_factory_status/", views.alter_factory_status, name='alter_factory_status'),
]