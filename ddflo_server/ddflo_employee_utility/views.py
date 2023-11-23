from django.shortcuts import render
from ddflo_employee_utility.models import *

# Create your views here.
def employee_home():
    pass

def fetch_employeeid_single(employeeID):
    return Employee.objects.filter(employeeid=employeeID).values('employeeid')

def fetch_employee_shiftgroup(shift_number):
    return Employee.objects.filter(shift_group=shift_number)

def get_available_employees(group_number, weekday):
    weekday_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    col_used = 'null'
    for weekdayiterator in weekday_list:
        if weekdayiterator == weekday:
            col_used = weekdayiterator
            break
    return Availability.objects.filter(employeeid=Employee.objects.filter(shift_group=group_number).values('employeeid'), **{col_used: 1}).values('employeeid')