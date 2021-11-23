from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['id']
    fields = (
        'description',
        'unit_price',
        'stock',
    )
    list_display = (
        'description',
        'unit_price',
        'stock',
    )
    readonly_fields = (
        'id',
    )
