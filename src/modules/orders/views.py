from rest_framework import viewsets, mixins
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
