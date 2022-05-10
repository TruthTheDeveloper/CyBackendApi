# from django.contrib.auth import get_user_model
import datetime
from datetime import timedelta
from django.utils import timezone
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField, CharField,IntegerField
from users.models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework.reverse import reverse as api_reverse

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# User = get_user_model()


class UserRegisterSerializer(ModelSerializer):
    password = CharField(style={'input_type':'password'}, write_only=True)
    token = SerializerMethodField(read_only=True)
    expires = SerializerMethodField(read_only=True)
    message = SerializerMethodField(read_only=True)
    status_code = SerializerMethodField(read_only=True)
    phone_number = IntegerField()

    class Meta:
        model =CustomUser
        fields = [
            'email', 
            'username',
            'phone_number',
            'token',
            'slug',
            'expires',
            'message',
            'status_code',
            'password'
        ]

        extra_kwargs = {'password': {'write_only':True}, 'email': {'required':True}}

    def validate_phone_number(self, value):
        return value#This actually print the value
        
    def get_status_code(self, obj):
        data = 200
        return data

    def get_message(self, obj):
        return 'Thank you for registering. Please verify your email before continuing'

    def get_token(self, obj):
        user = obj
        token = get_tokens_for_user(user)
        return token

    def validate_email(self,value):
        qs = CustomUser.objects.filter(email__iexact=value)
        if qs.exists():
            raise ValidationError("User with this email already exists")
        return value


    def validate_username(self, value):
        qs = CustomUser.objects.filter(username__iexact=value)
        if qs.exists():
            raise ValidationError("User with this username already exists")
        return value

 
    def create(self, validated_data):
        user_obj = CustomUser(
            username=validated_data.get('username'),
            email=validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj


    def get_expires(self, obj):
        return timezone.now() + timedelta(minutes=5) - datetime.timedelta(seconds=200)






