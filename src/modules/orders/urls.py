from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(prefix=r'api/orders', viewset=views.OrderViewSet,
                basename='orders')
urlpatterns = router.urls
