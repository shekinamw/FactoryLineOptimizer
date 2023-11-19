# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from ddflo_factory_management_utility.models import Factory

class Availability(models.Model):
    employeeid = models.OneToOneField('Employee', models.CASCADE, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    monday = models.IntegerField(db_column='Monday', blank=True, null=True)  # Field name made lowercase.
    tuesday = models.IntegerField(db_column='Tuesday', blank=True, null=True)  # Field name made lowercase.
    wednesday = models.IntegerField(db_column='Wednesday', blank=True, null=True)  # Field name made lowercase.
    thursday = models.IntegerField(db_column='Thursday', blank=True, null=True)  # Field name made lowercase.
    friday = models.IntegerField(db_column='Friday', blank=True, null=True)  # Field name made lowercase.
    saturday = models.IntegerField(db_column='Saturday', blank=True, null=True)  # Field name made lowercase.
    sunday = models.IntegerField(db_column='Sunday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'availability'


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apartment = models.CharField(db_column='Apartment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    provincestate = models.CharField(db_column='ProvinceState', max_length=2, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'employee'


class Performance(models.Model):
    workstationid = models.ForeignKey('Workstation', models.RESTRICT, db_column='WorkstationID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.CASCADE, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    employeeperformancescore = models.FloatField(db_column='EmployeePerformanceScore', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'performance'

class Workstation(models.Model):
    workstationid = models.IntegerField(db_column='WorkstationID', primary_key=True)  # Field name made lowercase.
    workstationname = models.CharField(db_column='WorkstationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    factory_id = models.ForeignKey(Factory, models.RESTRICT)

    class Meta:
        db_table = 'workstation'

class Wstask(models.Model):
    taskid = models.IntegerField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    workstationid = models.ForeignKey(Workstation, models.CASCADE, db_column='WorkstationID', blank=True, null=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='TaskName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'wstask'

class Schedule(models.Model):
    workstationid = models.OneToOneField('Workstation', models.RESTRICT, db_column='WorkstationID', primary_key=True)  # Field name made lowercase. The composite primary key (WorkstationID, EmployeeID, StartTime) found, that is not supported. The first column is selected.
    employeeid = models.ForeignKey(Employee, models.CASCADE, db_column='EmployeeID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'schedule'
        unique_together = (('workstationid', 'employeeid', 'starttime'),)


class Sensordata(models.Model):
    sensorid = models.IntegerField(db_column='SensorID', primary_key=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Wstask, models.CASCADE, db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    stopdatetime = models.DateTimeField(db_column='StopDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sensordata'
