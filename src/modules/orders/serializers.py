from rest_framework import serializers
from modules.inventory.models import Product
from .models import OrderProductDetail, Order


class OrderProductDetailSerializer(serializers.ModelSerializer):
    """Serializer for intermediary objects"""
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    unit_price = serializers.IntegerField()
    total = serializers.IntegerField()

    class Meta:
        model = OrderProductDetail
        fields = ('description', 'quantity', 'unit_price', 'total',)
        read_only_fields = ('id',)
        ordering = ('id',)


class OrderSerializer(serializers.Serializer):
    """Serializer for order objects"""
    items = serializers.ListField()

    def create(self, validated_data):
        """
        Overwriting the default `.create()` method.
        It allows calc `total` and `quantity` items and
        create OrderProductDetail object
        :param validated_data:
        :return: new order
        """
        items_list = validated_data['items']

        # init sum
        total_order = 0
        # new object
        new_order = Order.objects.create()

        # Tuple -> (Product, quantity)
        product_list = [(Product.objects.get(id=item['id']),
                         item['quantity']) for item in items_list]

        for product, quantity in product_list:
            # Sum total
            total = product.unit_price * quantity
            # Rest product's stock
            product.stock = product.stock - quantity
            # Save item
            product.save()

            # Creating object
            op_obj = OrderProductDetail(
                order=new_order, description=product.description,
                unit_price=product.unit_price, quantity=quantity, total=total)

            op_obj.save()

            total_order += total

        # Save total order
        new_order.total = total_order
        new_order.save()

        return new_order

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'items': OrderProductDetailSerializer(
                instance.products.all().order_by('id'), many=True).data,
            'total': instance.total
        }
