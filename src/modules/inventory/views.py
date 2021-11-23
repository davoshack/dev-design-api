from rest_framework import viewsets, mixins

from .models import Product
from . import serializers


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
