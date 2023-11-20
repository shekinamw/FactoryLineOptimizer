from django.db import models
from ddflo.models import *


class Sensordata(models.Model):
    sensorid = models.IntegerField(db_column='SensorID', primary_key=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Wstask, models.CASCADE, db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    stopdatetime = models.DateTimeField(db_column='StopDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sensordata'
