from rest_framework import viewsets
from .serializers import UserInfoSerializer
from userInfo.models import UserInfo


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    authentication_classes = []
    permission_classes = []
    queryset = UserInfo.objects.all()