from rest_framework import viewsets
from .serializers import UserInfoSerializer
from userInfo.models import UserInfo


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()