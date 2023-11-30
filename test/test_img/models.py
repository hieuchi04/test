from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    
    
def get_product_image_path(instance, filename):
    product_name = slugify(instance.product.title) if instance.product else "default"
    return f"product_image/{product_name}/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to=get_product_image_path)