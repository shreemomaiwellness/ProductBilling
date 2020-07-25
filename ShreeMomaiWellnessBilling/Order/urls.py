from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("CreateOrder/",views.CreateOrder, name="CreateOrder"),
    path("CreateOrderPostRequest/", views.CreateOrderPost, name="SubmitOrder"),
    path("Print/<int:Id>", views.PrintOrder, name="PrintOrder"),
]
