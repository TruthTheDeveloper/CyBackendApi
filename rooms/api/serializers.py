from rest_framework.serializers import ModelSerializer, ImageField
from rooms.models import Room

class RoomsSerializer(ModelSerializer):
    room_Image = ImageField()
    class Meta:
        model = Room
        fields = [
            "room_type",
            "room_description",
            "room_price",
            "room_Image",
            "created_at"
        ]