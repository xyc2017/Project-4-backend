from django.db import models

class Trips(models.Model):
    Country=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    From=models.DateField(auto_now=False)
    To=models.DateField(auto_now=False)
    Notes=models.CharField(max_length=1000)
    