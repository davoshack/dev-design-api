from django.db import models


class Order(models.Model):
    """Class that represents an order generated"""
    total = models.IntegerField(default=0)


class OrderProductDetail(models.Model):
    """Represents order -> detail items"""
    order = models.ForeignKey(Order, related_name='products', on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Order number: {self.order}"
