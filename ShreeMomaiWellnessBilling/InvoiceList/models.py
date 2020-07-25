from django.db import models
from Product.models import Product
from Order.models import Order

class ProductOrder(models.Model):
    Id = models.AutoField(primary_key=True)
    Fk_Product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    Fk_Order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    ProductCode = models.CharField(max_length=50,blank=False)
    UnitPrice = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2)
    AmountTaken = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2,null=True)
    Discount = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2, null= True)
    Quantity = models.PositiveSmallIntegerField(null=False)
    FinalAmount = models.DecimalField(blank=False, max_digits= 9, decimal_places= 2)

    class Meta:
        db_table = "Product Order"