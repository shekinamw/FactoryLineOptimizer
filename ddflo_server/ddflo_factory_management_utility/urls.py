from django.urls import path
from . import views

urlpatterns = [
   path("", views.factory_homepage, name="factory_homepage"),
   path("factory_homepage", views.factory_homepage, name="factory_homepage"),
   path("toggle/", views.toggle, name='toggle'),
]