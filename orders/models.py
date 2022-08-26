from operator import mod
from random import choices
from django.db import models
from django.contrib.auth.models import User 
from product.models import Product

# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_time=models.DateTimeField()
    name=models.CharField(max_length=255)
    address=models.TextField()
    payment=models.BooleanField(default=False)
    status=models.CharField(max_length=100,default='pending')

    def __str__(self):
        return str(self.id)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2)


    def __str__(self):
        return f'{self.order.id} - {self.product}'

class Payment(models.Model):
    pass