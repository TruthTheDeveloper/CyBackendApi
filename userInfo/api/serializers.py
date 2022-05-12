from rest_framework.serializers import ModelSerializer, SerializerMethodField
from userInfo.models import UserInfo


def create_full_name(title, firstname, lastname):
    return title + " " + firstname + " " + lastname


class UserInfoSerializer(ModelSerializer):
    full_name = SerializerMethodField(read_only=True)
    class Meta:
        model = UserInfo
        fields = [
            'title',
            'first_name',
            'last_name',
            'full_name',
            'phone_number',
            'email',
            'x_reservation',
            'discount_code',
            'check_in',
            'check_out',
            'payment_status',
            'confirm_user_lodge',
            'created_at'
        ]


    
    def get_full_name(self, obj):
        fullname = create_full_name(obj.title, obj.first_name, obj.last_name)
        return fullname
        