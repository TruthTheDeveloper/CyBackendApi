from rest_framework import viewsets
from .serializers import RoomsSerializer
from rooms.models import Room

class RoomsViewSet(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer
    queryset = Room.objects.all()