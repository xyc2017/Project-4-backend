from django.db import models

class Trips(models.Model):
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    dates=models.CharField(max_length=100)
    notes=models.CharField(max_length=1000)
    