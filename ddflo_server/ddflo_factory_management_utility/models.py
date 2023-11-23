from django.db import models

class Factory (models.Model):
    REAL = 'Real'
    SIMULATED = 'Simulated'
    FACTORY_TYPE_CHOICES = [
        (REAL, 'Real'),
        (SIMULATED, 'Simulated')
    ]
    factory_id = models.BigIntegerField(primary_key=True),
    factory_location = models.CharField(max_length=255, blank=False, null=False),
    factory_type =  models.CharField(max_length=255, choices=FACTORY_TYPE_CHOICES, default=SIMULATED)
    factory_status = models.BooleanField(default=False)
    class Meta:
        db_table = 'factory'

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
