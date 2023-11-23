from django.urls import path, register_converter, include
from . import views
from .views import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('<date:date>/', views.schedule_home, name='schedule_home'),
    path('', views.default_page, name='default_page'),
    path("navigate_date/", views.navigate_date, name="navigate_date"),
    path("create_schedule/", views.create_schedule, name="create_schedule"), 
]