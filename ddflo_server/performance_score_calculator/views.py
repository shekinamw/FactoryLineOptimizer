from django.shortcuts import render
from .models import Performance 
from datetime import date
from ddflo_factory_management_utility.views import * 

def fetch_top_employee_for_station(employee_list, workstation_id):
    return Performance.objects.filter(employeeid=employee_list, workstationoid=workstation_id).order_by("employeeperformancescore").first()

def fetch_top_employee_score(workstation_id):
    return Performance.objects.filter(workstationoid=workstation_id).order_by("employeeperformancescore").first()


def employee_at_station_in_schedule(halt_start, current_station):
    
    pass

# Calculate performance scores for an employee at a workstation
def generate_performance_score_individual(halt_start, halt_end, task_id): 
    halt_duration = halt_end - halt_start
    
    if halt_duration < 0:
        pass
        # Error handling, return

    # Where the halt happend
    # Provided the task_id -> workstation and get the station id
    current_workstation = fetch_workstation_based_on_task(task_id)
     
     # fetch_workstation_based_on_task(task_id) --> Define in factory management utility
    # Date when the halt happened
    shift_date = halt_start.date()
    # Get the employee working at the workstation that is halted 
    # fetch_employee_at_station_on_date_and_time
    current_employee = fetch_employee_based_on_station_and_date(current_workstation, halt_start)
    
    # Get the shift_duration for employee on date
    shift_duration = get_shift_duration(current_employee, shift_date)
    
    # Get's old performance
    initial_performance = fetch_performance(current_employee, current_workstation) 
    new_performance = initial_performance * (1 - (halt_duration/shift_duration))

    # Updates employee, workstation performance score
    Performance.objects.get(workstationid=current_workstation, employeeid=current_employee)
    Performance.employeeperformancescore=new_performance
    Performance.save()





