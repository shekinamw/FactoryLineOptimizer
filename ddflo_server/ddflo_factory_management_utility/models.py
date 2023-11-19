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
    class Meta:
        db_table = 'factory'