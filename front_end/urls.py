from django.urls import path 
from . import views
from product.models import ProductCategory


urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    #path('product-list/<int:catagory_id>', views.ProductListView.as_view(), name='ProductListView'),
     path('product-list', views.ProductListView.as_view(), name='ProductListView'),
]
