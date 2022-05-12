from .views import UserInfoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

app_name = "userInfo"

router.register(r'', UserInfoViewSet, basename='userInfo')
urlpatterns = router.urls