from django_filters.rest_framework import FilterSet
from .models import Product

class ProductFilters(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt']
        }

