# ddlo/urls.py
from django.urls import path
from . import views 
# urls.py


from .views import schedule_list



urlpatterns = [
   # path('landing_page/',views.landing_page, name='landing_page'),
    #path('calendar/',  views.calendar_view, name='calendar_view'),
    path("", views.home, name="home"),
    path("schedule/" , views.schedule_list, name="schedule_list")
    
]