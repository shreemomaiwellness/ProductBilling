from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList, name='ProductList'),
    path('Add/', views.Add, name='AddProduct'),
    path('Edit/<int:productId>',views.Edit,name = 'EditProduct')
]