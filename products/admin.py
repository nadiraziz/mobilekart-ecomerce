from django.contrib import admin
from .models import ProductCategory, Product, ProductImage, ProductBrand

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductBrand)

