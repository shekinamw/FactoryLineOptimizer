# ddflo/views.py
# ddflo/views.py
from django.shortcuts import render
from django.http import HttpResponse
from ddflo.models import *
from .models import  Schedule 

###########################################################################################
#################### Generating schedule based on performance #############################
###########################################################################################


@classmethod
def get_tasks_quality_score(cls, task_id):
    """
    1. get the taskID
    2. generate the quality score of the task
    3. return the quality score of the task
    4. loop through all the tasks in the workstation

    """
    return cls.objects.get(task_id=task_id).qualityscore
   
@classmethod
def get_tasks_time(cls, task_id):
    """
    1. get the taskID on the task table
    2. get the start time and end time of the task on the Wtask table
    2. get the start time and end time of the task on the sensordata table
    3. calculate the time spent on the task (end time - start time from Wstask table)
    4. calculate the stop time - start time from sensordata table
    5. calculate the total time spent on the task (time spent on the task + time spent on the task from sensordata table)
    6. return the total time spent on the task
    7. loop through all the tasks in the workstation
    """
    return cls.objects.get(task_id=task_id).time

@classmethod
def get_expected_task_score(cls, task_id):
    """
    Returns the expected task score of a task based on the factory's prediction for optimum productivity
    """
    return cls.objects.get(task_id=task_id).expectedtaskscore


@classmethod
def get_no_of_tasks(cls, task_id, workstation_id):
    """
    Returns the number of tasks in a workstation
    """
    return cls.objects.get(task_id=task_id,workstation_id=workstation_id).numberoftasks

@classmethod
def get_employee_performance_score(cls, employee_id):
    """
    Returns the performance score of an employee
    """
    #Formula: (Total time spent on a task / Expected time spent on a task) * (Quality score of a task / 100) * (Number of tasks in a workstation / 100))"
    
    
    # maybe we could also subtract from that (total stoped time/total time spent on a task)
    return cls.objects.get(employee_id=employee_id).employeeperformancescore

def schedule_list(request):
    context = {}
    all_schedules = Schedule.objects.all()
    context['schedules'] = all_schedules
    return render(request, 'schedule.html', context)


def home(request):
     return render (request, "base.html")


def calendar_view(request):
    # Your existing calendar view logic
    # ...
    return render(request, 'ddflo/calendar_view.html')

