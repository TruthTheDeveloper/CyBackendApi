from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import AuthView, RegisterAPIView

app_name='users'

urlpatterns = [
    path('', AuthView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterApiViews.as_view()),
    # path('refresh/', refresh_jwt_token),
]


