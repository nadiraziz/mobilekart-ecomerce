from rest_framework import serializers
from .models import ProductCategory, Product, ProductBrand



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
        
class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id')

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'category_id', 'quantity', 'description', 'product_brand', 'created_at', 'updated_at']
        

