from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Login, name = "Login"),
    path('Logout/', views.Logout, name = "Logout"),
    path("InvoiceList/", views.InvoiceList, name = "InvoiceList")
]
