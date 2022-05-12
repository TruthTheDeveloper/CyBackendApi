from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from .permissions import AnonPermissionOnly
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from datetime import timedelta
from django.utils import timezone
from users.models import CustomUser

def get_tokens_for_user(user, message, status):
    refresh = RefreshToken.for_user(user)

    return {
        'id':user.id,
        'username':user.username,
        'email':user.email,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message':message,
        'status':status,
        'expires':timezone.now() + timedelta(minutes=5) - datetime.timedelta(seconds=200)
    }

User = get_user_model()

class AuthView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args,  **kwargs):
        if request.user.is_authenticated:
            return Response({'detail':'You are already authenticated'}, status=400)
        data = request.data
        print(request.data, 'data')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        print(user, 'user')
        qs = User.objects.filter(
            Q(username__iexact=email)|
            Q(email__iexact=email)
        ).distinct()
        print(qs, 'qs')
        if qs.count() == 1:
            user_obj = qs.first()
            print(user_obj)
            message = "Successfull"
            status_code = 200
            response = get_tokens_for_user(user, message, status_code)
            return Response(response)
        else:
            return Response({'detail':'Invalid credentials'}, status=401)




class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    # permission_classes = [AnonPermissionOnly]
    # authentication_classes = []
    permission_classes = [AnonPermissionOnly]


    # def post(self, request):
        
    #     username = request.data.get("username")
    #     email = request.data.get("email")
    #     phone_number = request.data.get("phone_number")
    #     password = request.data.get("password")
    #     slug = request.data.get('slug')


    #     data = {"email":email, "username":username, "slug":slug, "password": password, "phone_number":phone_number}

        

    #     serializer =  UserRegisterSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()

    #     CustomUser.objects.create(**serializer.validated_data)
       

       

    #     return Response(data, status=201)



# {"email":"Alex@gmail.com", "password":"vocabulary1@"}