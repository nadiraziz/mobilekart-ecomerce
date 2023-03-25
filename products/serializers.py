from rest_framework import serializers
from .models import ProductCategory, Product



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
        

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id')

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'category_id']
