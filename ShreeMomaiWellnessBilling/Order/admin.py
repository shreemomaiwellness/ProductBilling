from django.contrib import admin
from .models import Customer,Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("Customer_Id","FirstName","LastName","Email","Phone","City","PinCode")
    empty_value_display = "NULL"

class OrderAdmin(admin.ModelAdmin):
    list_display = ("Order_Id","FK_Customer__Id", "Date", "TotalAmount","IsCash", "IsCheque", "BankName", "ChequeNo","IsOnline","PlatformName","TransactionId")
    empty_value_display = "NULL"

    def FK_Customer__Id(self, instance):
        return instance.FK_Customer_Id.Customer_Id

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
