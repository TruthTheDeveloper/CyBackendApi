from rest_framework import viewsets
from .serializers import RoomsSerializer
from rooms.models import Room

# class RoomsViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     permission_classes = []
#     serializer_class = RoomsSerializer
#     queryset = Room.objects.all()



class RoomsViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = RoomsSerializer
    

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Room.objects.all()
        available = self.request.query_params.get('available')
        if available is not None:
            queryset = queryset.filter(available=available)
        return queryset