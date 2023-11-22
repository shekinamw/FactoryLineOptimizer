from django.db import models
from ddflo_employee_utility.models import Employee
from ddflo_factory_management_utility.models import Workstation


class Performance(models.Model):
    workstationid = models.ForeignKey(Workstation, models.RESTRICT, db_column='WorkstationID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.CASCADE, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeeperformancescore = models.FloatField(db_column='EmployeePerformanceScore', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'performance'