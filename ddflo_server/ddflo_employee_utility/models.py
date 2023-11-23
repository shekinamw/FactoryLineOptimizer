from django.db import models
from ddflo_factory_management_utility.models import *
from django.db import models

class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shift_group = models.IntegerField(db_column='ShiftGroup', blank=True, null=True)
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

class Availability(models.Model):
    employeeid = models.OneToOneField(Employee, models.CASCADE, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    monday = models.IntegerField(db_column='Monday', blank=True, null=True)  # Field name made lowercase.
    tuesday = models.IntegerField(db_column='Tuesday', blank=True, null=True)  # Field name made lowercase.
    wednesday = models.IntegerField(db_column='Wednesday', blank=True, null=True)  # Field name made lowercase.
    thursday = models.IntegerField(db_column='Thursday', blank=True, null=True)  # Field name made lowercase.
    friday = models.IntegerField(db_column='Friday', blank=True, null=True)  # Field name made lowercase.
    saturday = models.IntegerField(db_column='Saturday', blank=True, null=True)  # Field name made lowercase.
    sunday = models.IntegerField(db_column='Sunday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'availability'