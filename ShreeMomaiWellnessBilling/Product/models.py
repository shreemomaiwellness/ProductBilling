from django.db import models

class Product(models.Model):
    Id = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=50,blank=False)
    UnitPrice = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2)
    Quantity_abbr = models.CharField(max_length=5,null=True)
    CreatedOn = models.DateTimeField(blank=False)
    UpdatedOn = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "Product"