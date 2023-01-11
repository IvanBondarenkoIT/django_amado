from django.db import models


# Create your models here.
class ProductsBrand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class ProductsCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Products(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(max_length=10)
    rating = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_img/%Y/%m/%d', blank=True)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductsBrand, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
