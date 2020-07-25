from django.shortcuts import render, redirect
from Order.models import Order
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def InvoiceList(request):
    if request.user.is_authenticated:
        OrderList = Order.objects.all().order_by("-Date")
        Context = {"OrderList":OrderList}
        return render(request, "InvoiceList/invoiceList.html",Context)
    else:
        messages.error(request, "Invalid username or password.")
        return render(request,"InvoiceList/Login.html")

def Login(request):
    if request.user.is_authenticated:
        return redirect('InvoiceList')
    else:
        if request.method == 'POST':
            username = request.POST.get('UserName')
            password = request.POST.get('Password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("/InvoiceList")
            else:
                messages.error(request, "Invalid username or password.")
                return render(request,"InvoiceList/Login.html")
        else:
            return render(request,"InvoiceList/Login.html")

def Logout(request):
    logout(request)
    return redirect("/")
