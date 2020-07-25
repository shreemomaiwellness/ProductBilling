from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("Id","ProductName","UnitPrice","Quantity_abbr","CreatedOn","UpdatedOn")
    empty_value_display = "NULL"

admin.site.register(Product,ProductAdmin)
