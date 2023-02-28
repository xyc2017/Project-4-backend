from django.db import models

class Trips(models.Model):
    Country=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    From=models.DateField(auto_now=True)
    To=models.DateField(auto_now=True)
    Notes=models.CharField(max_length=1000)
    