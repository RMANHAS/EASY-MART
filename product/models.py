from django.db import models

class ProductCategory(models.Model):
    name=models.CharField(max_length=225)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,related_name="Product")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField()
    sku = models.CharField(max_length=20)
    cover_image = models.ImageField()
    status = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField()

    def __str__(self):
        return self.product.name