from django.db import models

class Trips(models.Model):
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    datefrom=models.DateField
    dateto=models.DateField
    notes=models.CharField(max_length=1000)
    