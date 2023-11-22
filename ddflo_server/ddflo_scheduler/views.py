from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from performance_score_calculator import views
from ddflo_employee_utility.views import * 
from django.db.models import F
# from ddflo_optimizer.views import function_I_want_to_use (<< that's a placeholder)
# from ddflo_employee_utility.views import 

''''

DateConverter is complete

'''

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format1 = '%Y-%m-%d'
    format2 = '%b. %d, %Y'

    def to_python(self, value):
        try:
            placeholder = datetime.strptime(value, self.format1).date()
            return placeholder
        except ValueError:
            try:
                return datetime.strptime(value, self.format2).date()
            except ValueError:
                return None   

    # Potential issue here calling strftime
    def to_url(self, value):
        return value.strftime(self.format1)

''''
Schedule_home is complete
'''
def schedule_home(request, date):
    # Paramter date taken from 
    get_schedule = fetch_schedule(date)
    json_date = {'date' : date}
    
    if get_schedule.exists():
        shift_structure = fetch_shift_structure()
        context = {'shift_structure': shift_structure, 'date': date}

        for shift in shift_structure:
            placeholder = fetch_employee_shiftgroup(map_shiftname_to_groupnumber(shift['shiftname']))
            context[shift['shiftname']] = placeholder
        return render(request, 'schedule_home.html', get_schedule, context)
    else:
        context = {'date': date}
        return render(request, 'no_schedule.html', context)

'''
Default page is complete
'''

def default_page(request):
    current_date = datetime.now().date()
    return redirect('schedule_home', date=current_date)

'''
Navigate Date is complete
'''

def navigate_date(request):
    direction = request.POST.get('direction')
    date_str = request.POST.get('date')

    python_date = DateConverter().to_python(date_str)
    if direction == 'forward':
        next_date = python_date + timedelta(days=1)
    elif direction == 'backward':
        next_date = python_date - timedelta(days=1)
    else:
        next_date = datetime.now()

    # Redirect to the schedule_home view with the next date
    return redirect('schedule_home', date=next_date)

def fetch_shift_structure():
    return Shift.objects.all().order_by('start_time').values()


'''
fetch_schedule is complete
'''

def fetch_employee_based_on_station_and_date(workstation, date):
    #Getting the shiftname from the shifts table that is within the range of date (date is in time format)
    shift_number_in_halt_time = Shifts.objects.filter(start_time__gte=date.strftime('%H:%M:%S'), end_time__lte=date.strftime('%H:%M:%S')).values('shiftname')
    # Get employees that work at workstation on halt date (needs)
    return Schedule.objects.filter(workstationid=workstation, shiftdate=date.date(), shiftgroup=shift_number_in_halt_time).values('employeeid')

 


def fetch_schedule(date):
    return Schedule.objects.filter(shift_date=date).values()

# Will take a shift date and generation_type (e.g. automatic, manual) as input
def create_schedule(request): #generation_type):
    generation_startdate = DateConverter().to_python(request.POST.get('date'))
    generation_enddate = generation_startdate + timedelta(days=7)
    
    if not generate_optimized_schedule(generation_startdate, generation_enddate):
        # return redirect('/error_page/')
        pass
    else:
        return redirect('schedule_home', date=generation_startdate)

'''
map_shiftname_top_groupnumber is complete
'''
def map_shiftname_to_groupnumber(shiftname):
    ShiftGroup.objects.filter(shift_name=shiftname).values('group_number')


def get_shift_duration(employee_id, shift_date):
    start_time, end_time = get_shift_start_end(employee_id, shift_date)
    
    # Calculate duration
    if start_time and end_time:
        start_time = start_time['start_time']
        end_time = end_time['end_time']

        # If the shift ends before it starts on the same day, assume it spans to the next day
        if end_time < start_time:
            end_time += timedelta(days=1)

        shift_duration = end_time - start_time
        return shift_duration


def  get_shift_start_end(employee_id, shift_date):
    # Assuming Shift model has fields 'shiftname', 'start_time', and 'end_time'
    shifts = Shift.objects.filter(
        shiftname__in=ShiftGroup.objects.filter(
            group_number=Employee.objects.filter(employeeid=employee_id).values('shift_group_id')
        ).values('shift_name_id'),
    )

    # Assuming shift_date is a datetime object
    shifts_on_date = shifts.filter(shift_date=shift_date)

    # Assuming the start_time and end_time are DateTimeFields in the Shift model
    start_time = shifts_on_date.aggregate(start_time=F('start_time'))
    end_time = shifts_on_date.aggregate(end_time=F('end_time'))

    return start_time, end_time

    # Return None if no shift found on the given date
    return None
