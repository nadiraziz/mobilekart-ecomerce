from django.db import models
import uuid



class ProductCategory(models.Model):
    """ model representing product categories """
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name
    

class ProductBrand(models.Model):
    """ model representing product categories """
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product brand'
        verbose_name_plural = 'product brand'

    def __str__(self):
        return self.name

   
# product model
class Product(models.Model):
    """ model representing ecommerce products """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    product_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
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
    
