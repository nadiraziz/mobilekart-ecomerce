from django.urls import path
from .views import ProductListView, ProductCategoryListView

urlpatterns = [
    # product categories
    path('product-categories/', ProductCategoryListView.as_view(), name='product-category-list'),
    path('product-categories/<uuid:pk>/', ProductCategoryListView.as_view(), name='product-category-detail'),
    
    
    # products
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<uuid:pk>/', ProductListView.as_view(), name='product-detail'),
]
