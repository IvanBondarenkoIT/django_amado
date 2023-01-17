from django.db import models
import uuid
import os


class ProductsBrand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'name')


class ProductsCategory(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    # photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'name')


class Product(models.Model):

    def get_file_name(self, filename: str) -> str:
        """Create unique name to save image"""
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/products', filename)

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    rating = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)

    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductsBrand, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.price}$ - {self.brand}'

    class Meta:
        ordering = ('rating', 'category', 'name')

    def grt_absolute_url(self):
        return reversed("shop:product_datails", srgs=[self.id, self.slug])

    def get_raying_as_range(self):
        return range(self.rating)
