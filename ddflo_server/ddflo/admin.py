from django.contrib import admin
from .models import  Factory,Availability,Employee,Performance,Workstation,Wstask,Schedule,Sensordata

# Register your models here.
admin.site.register(Employee)
admin.site.register(Schedule)
admin.site.register(Factory)
admin.site.register(Availability)
admin.site.register(Performance)
admin.site.register(Workstation)
admin.site.register(Wstask)
admin.site.register(Sensordata)
