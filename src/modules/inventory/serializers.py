import ipdb
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for products objects"""

    class Meta:
        model = Product
        fields = ('id', 'description', 'unit_price', 'stock',)
        read_only_fields = ('id',)
