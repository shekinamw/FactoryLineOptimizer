from django.db import models
from ddflo_factory_management_utility.models import Wstask


class Sensordata(models.Model):
    sensorid = models.AutoField(db_column='SensorID', primary_key=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Wstask, models.CASCADE, db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    haltstart = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    haltend = models.DateTimeField(db_column='StopDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sensordata'
