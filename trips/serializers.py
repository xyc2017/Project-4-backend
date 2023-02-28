from .models import Trips
from rest_framework import serializers

# TripsSerializer
class TripsSerializer(serializers.HyperlinkedModelSerializer): ## gives us json
    class Meta:
        # the model it will serialize
        model=Trips
        # the fields that should be included in the serialized output
        fields=['id','country','city','from','to','notes' ]