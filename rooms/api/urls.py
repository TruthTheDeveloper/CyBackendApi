from .views import RoomsViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

app_name = "rooms"

router.register(r'', RoomsViewSet, basename='rooms')
urlpatterns = router.urls