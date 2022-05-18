from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from rooms.models import Room

class RoomsSerializer(ModelSerializer):
    room_Image = ImageField()
    id = SerializerMethodField(read_only=True)
    class Meta:
        model = Room
        fields = [
            'id',
            "room_type",
            "room_description",
            "room_price",
            "room_Image",
            "created_at",
            "available"
        ]


    def get_id(self,obj):
        return obj.id