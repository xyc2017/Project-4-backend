from .models import Trips
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TripsSerializer

class TripsViewSet(viewsets.ModelViewSet):
    ## main query for the index route
    queryset=Trips.objects.all()
    ## serializer class for serializing output
    serializer_class=TripsSerializer
    ## optional permission class set permission level
    permission_classes=[permissions.AllowAny] # or [permissions.IsAuthenticated]