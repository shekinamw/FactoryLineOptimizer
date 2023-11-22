from django.shortcuts import render
from ddflo_sensor_data_utility.views import *
from ddflo_employee_utility.views import get_available_employees
from ddflo_factory_management_utility.views import fetch_factory_all, fetch_all_workstations
from performance_score_calculator.views import *
from ddflo_scheduler.views import fetch_shift_structure, map_shiftname_to_groupnumber


def generate_daily_schedule(date):
    # Iterate through a list of workstations
    workstation_list = fetch_all_workstations()
    list_of_elim_employees = []
    generation_outcome = True
    schedule_records = []
    
    for shift in fetch_shift_structure():
        # Maps the shiftname to the groupnumber, so we can connect the group number to the employee
        group_number = map_shiftname_to_groupnumber(shift.shiftname)

        # Gets all the employees available on the start date provided by the user via the scheduler application
        weekday_format = date.strftime('%A').lower()
        available_employees = get_available_employees(group_number, weekday_format)
        
        # Check if available_employees is empty or not enough for each workstation
        if not available_employees.exists() or available_employees.count() < workstation_list.count():
            generation_outcome = False
            break

        # Get the best employee based on score for each workstation
        for workstation in workstation_list:
            # Check if the available_employee is in list_of_elim_employees
            if available_employees.filter(employee_id__in=list_of_elim_employees).exists():
                continue  # Move to the next workstation if already processed

            top_employee = fetch_top_employee_for_station(available_employees, workstation)
            list_of_elim_employees.append(top_employee)
            
            # Assuming 'schedule' is your model
            schedule_record = Schedule(
                workstationid=workstation,
                employeeid=top_employee,
                shift_date=date
            )
            schedule_records.append(schedule_record)

    # Execute the creation after completing the main loop
    if generation_outcome:
        Schedule.objects.bulk_create(schedule_records)
        
    return generation_outcome
    
# Returns 1 if successful and 0 otherwise
def generate_optimized_schedule(start_date, end_date):
    current_date = start_date
    optimized_schedule = []
    generation_outcome = None

    # Iterate through the date range and generate daily schedules
    while current_date <= end_date:
        # Call generate for the day
        if not generate_daily_schedule(current_date):
            generation_outcome = current_date 
            break
        # Move to the next day
        current_date += timedelta(days=1)

    # Return the optimized schedule for the entire date range
    return generation_outcome
 
