from django.shortcuts import render, redirect
from Product.models import Product
from InvoiceList.models import ProductOrder
from .models import Order, Customer
from django.utils import timezone
from django.contrib import messages
from num2words import num2words as word
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/')
def CreateOrder(request):
    Products = Product.objects.all().order_by("Id")
    Context = {"Products": Products}
    return render(request, "Order/CreateOrder.html", Context)


@login_required(login_url='/')
def CreateOrderPost(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        deliveryDate = request.POST.get('DeliveryDate')

        ProductIds = request.POST.getlist('product')
        Quantities = [i for i in request.POST.getlist('Quantity') if i]
        Discounts = [i for i in request.POST.getlist('Discount') if i]
        Amounts = [i for i in request.POST.getlist('AmountTaken') if i]
        ProductCode = [i for i in request.POST.getlist('ProductCode') if i]


        discount_check = request.POST.get('discount-check')
        amount_take = request.POST.get('amount-take')

        FinalAmount = 0

        if discount_check == "Discount":
            for p, q, d in zip(ProductIds, Quantities, Discounts):
                product = Product.objects.get(Id=p)
                PartialAmount = product.UnitPrice - ((product.UnitPrice * eval(d)) / 100)
                FinalAmount = FinalAmount + (PartialAmount * eval(q))
        if amount_take == "Amount":
            for p, q, a in zip(ProductIds, Quantities, Amounts):
                PartialAmount = eval(a) * eval(q)
                FinalAmount = FinalAmount + PartialAmount
        if discount_check == None and amount_take == None:
            for p, q in zip(ProductIds, Quantities):
                product = Product.objects.get(Id=p)
                PartialAmount = product.UnitPrice * eval(q)
                FinalAmount = FinalAmount + PartialAmount
        PaymentMode = request.POST.get('PaymentMode')
        BankName = request.POST.get('BankName')
        ChequeNo = request.POST.get('ChequeNo')
        OnlinePlatform = request.POST.get('OnlineMedium')
        TransactionId = request.POST.get('TransactionId')

        customer = Customer.objects.create(FirstName=fname, MiddleName=mname, LastName=lname, Address1=address1,
                                           Address2=address2, City=city, PinCode=pincode, Phone=phone, Email=email)
        customer.save()
        if PaymentMode == "Cash":
            order = Order.objects.create(FK_Customer_Id=customer, Date=timezone.now(), IsCash=True,
                                         DeliveryDate=deliveryDate,
                                         TotalAmount=FinalAmount)
        if PaymentMode == "Cheque":
            order = Order.objects.create(FK_Customer_Id=customer, Date=timezone.now(), IsCheque=True, BankName=BankName,
                                         DeliveryDate=deliveryDate,
                                         ChequeNo=ChequeNo, TotalAmount=FinalAmount)
        if PaymentMode == "Online":
            order = Order.objects.create(FK_Customer_Id=customer, Date=timezone.now(), IsOnline=True,
                                         PlatformName=OnlinePlatform, TransactionId=TransactionId,
                                         DeliveryDate=deliveryDate,
                                         TotalAmount=FinalAmount)

        order.save()

        if discount_check == "Discount":
            for p, q, d, pc in zip(ProductIds, Quantities, Discounts, ProductCode):
                product = Product.objects.get(Id=p)
                AmountTaken = (product.UnitPrice - ((product.UnitPrice * eval(d)) / 100))
                PartialAmount = AmountTaken * eval(q)
                productorder = ProductOrder.objects.create(Fk_Product=product, Fk_Order=order,
                                                           UnitPrice=product.UnitPrice, Discount=eval(d),
                                                           Quantity=eval(q), AmountTaken=AmountTaken,
                                                           ProductCode=pc.strip(),
                                                           FinalAmount=PartialAmount)
                productorder.save()
        if amount_take == "Amount":
            for p, q, a, pc in zip(ProductIds, Quantities, Amounts, ProductCode):
                product = Product.objects.get(Id=p)
                PartialAmount = eval(a) * eval(q)
                Discount = (100 * (product.UnitPrice - eval(a))) / product.UnitPrice
                productorder = ProductOrder.objects.create(Fk_Product=product, Fk_Order=order,
                                                           UnitPrice=product.UnitPrice, AmountTaken=eval(a),
                                                           Discount=Discount, Quantity=eval(q),
                                                           ProductCode=pc.strip(),
                                                           FinalAmount=PartialAmount)
                productorder.save()
        if discount_check == None and amount_take == None:
            for p, q, pc in zip(ProductIds, Quantities, ProductCode):
                product = Product.objects.get(Id=p)
                PartialAmount = product.UnitPrice * eval(q)
                productorder = ProductOrder.objects.create(Fk_Product=product, Fk_Order=order,
                                                           UnitPrice=product.UnitPrice, AmountTaken=product.UnitPrice,
                                                           Discount=0, Quantity=eval(q),
                                                           ProductCode=pc.strip(),
                                                           FinalAmount=PartialAmount)
                productorder.save()
    messages.add_message(request, messages.SUCCESS, "Order Created SuccesFully")

    return redirect('InvoiceList')


@login_required(login_url='/')
def PrintOrder(request, Id):
    OrderData = Order.objects.get(Order_Id=Id)
    CustomerData = Customer.objects.get(Customer_Id=OrderData.FK_Customer_Id.Customer_Id)
    ProductOrderData = ProductOrder.objects.all().filter(Fk_Order=OrderData)
    AmountInWords = word(OrderData.TotalAmount)
    Context = {
        "Today": timezone.now(),
        "Order": OrderData,
        "Customer": CustomerData,
        "ProductOrder": ProductOrderData,
        "AmountInWords": AmountInWords
    }
    return render(request, "Order/PrintOrder.html", Context)
