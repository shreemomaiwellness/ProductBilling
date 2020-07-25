from django.contrib import admin
from .models import ProductOrder

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ("Id","FK_Order_Id","FK_Product_Name","Quantity","UnitPrice", "Discount","AmountTaken", "FinalAmount")
    empty_value_display = "NULL"

    def FK_Product_Name(self, instance):
        return instance.Fk_Product.ProductName

    def FK_Order_Id(self, instance):
        return instance.Fk_Order.Order_Id

admin.site.register(ProductOrder,ProductOrderAdmin)
