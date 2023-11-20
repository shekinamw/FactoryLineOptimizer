from django.urls import path, include
from . import views

urlpatterns = [
    path("factory_homepage", views.factory_homepage, name="factory_homepage"),
]