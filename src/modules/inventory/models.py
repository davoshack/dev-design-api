from django.db import models


class Product(models.Model):
    """Product object"""
    description = models.CharField(max_length=255, blank=False, null=False)
    unit_price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"Description: {self.description}"
