# from django.contrib.auth import get_user_model
import datetime
from datetime import timedelta
from django.utils import timezone
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, IntegerField, EmailField, ValidationError
from users.models import CustomUser


from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework.reverse import reverse as api_reverse



class UserRegisterSerializer(ModelSerializer):
    password = CharField(style={'input_type':'password'}, write_only=True)
    message = SerializerMethodField(read_only=True)
    email = EmailField()
    # phone_number = IntegerField()

    class Meta:
        model =CustomUser
        fields = [
            'email', 
            'username',
            'phone_number',
            'message',
            'password'
        ]

        extra_kwargs = {'password': {'write_only':True}, 'email': {'required':True}}

    def validate_phone_number(self, value):
        return value#This actually print the value
        

    def get_message(self, obj):
        return 'Thank you for registering. Please verify your email before continuing'

    def validate_email(self,value):
        qs = CustomUser.objects.filter(email__iexact=value)
        print(qs)
        if qs.exists():
            raise ValidationError("User with this email already exist")
        return value

    def validate_username(self, value):
        qs = CustomUser.objects.filter(username__iexact=value)
        if qs.exists():
            raise ValidationError("User with this username already exist")
        return value

 
    def create(self, validated_data):
        user_obj = CustomUser(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            phone_number=validated_data.get('phone_number')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj








