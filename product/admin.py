from argparse import Action
from cmath import e
from email import message
from itertools import product
from logging import exception
from pyexpat import model
from telnetlib import STATUS
from tkinter import E
from django.contrib import admin,messages

from product.models import ProductCategory,Product,ProductImage
# Register your models here.

def active_status(modeladmin,request,queryset):
    try:
        queryset.update(status=True)
        messages.success(request,'successfully active')
    except Exception as e:
        messages.error(request,str(e))


def inactive_status(modeladmin,request,queryset):
    try:
        queryset.update(status=False)
        messages.success(request,'successfully inactive')
    except Exception as e:
        messages.error(request,str(e))

class ProductImageinline(admin.TabularInline):
    model=ProductImage


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['name','status']
    list_filter=('status',)
    search_fields=['name',]
    actions = [active_status,inactive_status]
    

admin.site.register(ProductCategory,ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','product_category','price','stock','status']
    list_filter=['status','product_category']
    search_field=('name','sku')
    actions = [active_status,inactive_status]
    inlines=[ProductImageinline,]


admin.site.register(Product,ProductAdmin)