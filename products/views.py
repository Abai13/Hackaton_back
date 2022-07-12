from django.shortcuts import render

from rest_framework.viewsets import (ModelViewSet)
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filterset_fields = ['category', 'price']


    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()
        