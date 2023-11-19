from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.factory_homepage, name="factory_homepage"),
]