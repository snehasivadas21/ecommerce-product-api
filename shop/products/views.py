from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "product_list"
        data = cache.get(cache_key)

        if not data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60)  

        return Response(data)
    
    def perform_create(self, serializer):
        serializer.save()
        cache.delete("product_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("product_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("product_list")