from django.db import models
import uuid


# class ProductCategory(models.Model):
#     product_category_id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False) 
#     category_name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.category_name


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name

   


# product model
class Product(models.Model):
    """ model representing ecommerce products """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    product_name = models.CharField(max_length=200, blank=False, null=False)
    # product_category = models.OneToOneField(ProductCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    @property
    def category_id(self):
        return self.category.id
    
    
    
class ProductImage(models.Model):
    product = models.ManyToManyField(Product, related_name='product_images')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)