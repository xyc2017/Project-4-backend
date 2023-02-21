from .models import Trips
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# TripsSerializer
class TripsSerializer(serializers,HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model=Trips
        # the fields that should be included in the serialized output
        fields=['id','country','city','datefrom','dateto','notes' ]