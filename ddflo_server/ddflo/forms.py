# forms.py
from django import forms
from django.forms import DateTimeInput
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['workstationid', 'employeeid', 'starttime', 'endtime']
        widgets = {
            'starttime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'endtime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
