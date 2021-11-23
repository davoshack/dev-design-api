from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(prefix=r'api/products', viewset=views.ProductViewSet,
                basename='products')

urlpatterns = router.urls
