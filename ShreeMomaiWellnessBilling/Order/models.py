from django.db import models

class Customer(models.Model):
    Customer_Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255,blank=False)
    MiddleName = models.CharField(max_length=255,blank=False)
    LastName = models.CharField(max_length=255,blank=False)
    Address1 = models.CharField(max_length=500,blank=False)
    Address2 = models.CharField(max_length=500,blank=False)
    City = models.CharField(max_length=255,blank=False)
    PinCode = models.CharField(max_length=255,blank=False)
    Phone = models.CharField(max_length=13,blank=False)
    Email = models.CharField(max_length=310,blank=False)

    class Meta:
        db_table = "Customer"

class Order(models.Model):
    Order_Id = models.AutoField(primary_key=True)
    FK_Customer_Id = models.ForeignKey(Customer,blank=False,on_delete=models.CASCADE)
    Date = models.DateTimeField(blank=False)
    IsCash = models.BooleanField(default=False)
    IsCheque = models.BooleanField(default=False)
    BankName = models.CharField(max_length=255, blank=True, null=True)
    ChequeNo = models.CharField(max_length=255, blank=True, null=True)
    IsOnline = models.BooleanField(default=False)
    PlatformName = models.CharField(max_length=255, blank=True,null=True)
    TransactionId = models.CharField(max_length=500, blank=True,null=True)
    TotalAmount = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2)
    DeliveryDate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "Order"