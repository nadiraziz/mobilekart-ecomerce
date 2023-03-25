from django.shortcuts import render
from .models import Product,  ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated


class ProductListView(GenericAPIView, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request ,*args,**kwargs):
        return self.list(request ,*args,**kwargs)
    
    def post(self, request ,*args,**kwargs):
        return self.create(request ,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
    


class ProductCategoryListView(GenericAPIView, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get(self, request ,*args,**kwargs):
        return self.list(request ,*args,**kwargs)
    
    def post(self, request ,*args,**kwargs):
        return self.create(request ,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
    