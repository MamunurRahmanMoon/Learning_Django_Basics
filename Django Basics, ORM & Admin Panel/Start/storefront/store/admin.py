from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Aggregate, Count, Avg, Sum
from django.http.request import HttpRequest
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'collection__title']
    list_editable = ['unit_price']
    list_per_page = 15
    list_select_related = ['collection']

    def collection__title(self, product):
        return product.collection.title

# admin.site.register(models.Collection)
@admin.register(models.Collection)
class collectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

@admin.register(models.Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 15
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

@admin.register(models.Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer']
    list_per_page = 15
    

