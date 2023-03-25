from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated


class ProductListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request ,*args,**kwargs):
        return self.list(request ,*args,**kwargs)
    
    def post(self, request ,*args,**kwargs):
        return self.create(request ,*args,**kwargs)