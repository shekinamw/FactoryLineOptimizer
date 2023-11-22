from django.db import models

class Shift(models.Model):
    MORNING = 'Morning'
    AFTERNOON = 'Afternoon'
    EVENING = 'Evening'
    SHIFT_NAME_OPTIONS = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening')
    ]
    shiftname = models.CharField(max_length=255, choices=SHIFT_NAME_OPTIONS, primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = "shift"

class ShiftGroup(models.Model):
    group_number = models.SmallIntegerField(primary_key=True)
    shift_name = models.OneToOneField(Shift, on_delete=models.PROTECT)

    class Meta:
        db_table = "shiftgroup"

class Schedule(models.Model):
    surrogate_id = models.AutoField(primary_key=True, default=1)
    workstationid = models.OneToOneField('ddflo_factory_management_utility.Workstation', models.RESTRICT, db_column='WorkstationID')
    employeeid = models.ForeignKey('ddflo_employee_utility.Employee', on_delete=models.CASCADE, db_column='EmployeeID')
    shift_date = models.DateField(db_column='ShiftDate')

    class Meta:
        db_table = 'schedule'
        unique_together = (('workstationid', 'employeeid', 'shift_date'))