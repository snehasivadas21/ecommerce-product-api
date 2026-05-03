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
        page = request.query_params.get('page', 1)
        cache_key = f"product_list_{page}"

        data = cache.get(cache_key)

        if not data:
            response = super().list(request, *args, **kwargs)  
            cache.set(cache_key, response.data, timeout=60)
            return response

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