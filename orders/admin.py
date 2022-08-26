from re import search
from django.contrib import admin
from . models import Order,OrderDetails

# Register your models here.
class OrderInline(admin.TabularInline):
    model = OrderDetails
    extra = 1
    classes = ['collapse']


class OrdersAdmin(admin.ModelAdmin):
    list_display=['name','id','date_time','payment','status']
    list_filter = ['payment','status']
    search_fields = ['id','name']
    date_hierarchy = 'date_time'
    inlines = [OrderInline]

admin.site.register(Order,OrdersAdmin)