from acc.forms import OrderForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *


def main(request):
    return render(request,'acc/main.html')
def home(request):
    return render(request,'acc/main.html')

def admin_dashboard(request):
    return render(request,'acc/admin_dashboard.html')

def stockRedirect(request):
    return redirect('acc/stock.html')


def customers(request):
    return render(request,'acc/customers.html')

def products(request):
    products=Product.objects.all()
    return render(request,'acc/products.html',{'list':products})

def stock(request):
    return render(request,'acc/stock.html')


def navbar(request):
    return render(request,'acc/navbar.html')

def purchases(request):
    return render(request,'acc/purchases.html')

def footer(request):
    return render(request,'acc/footer.html')
def reports(request):
    return render(request,'acc/reports.html')

def sign_in(request):
    return render(request,'acc/sign_in.html')

def sign_up(request):
    return render(request,'acc/sign_up.html')

def user_accounts(request):
    return render(request,'acc/user_accounts.html')

def deployment(request):
    return render(request,'acc/deployment.html')

def vendors(request):
    return render(request,'acc/vendors.html')

def requests(request):
    return render(request,'acc/requests.html')

def returns(request):
    return render(request,'acc/returns.html')    

def about(request):
    return render(request,'acc/about.html')  

def services(request):
    return render(request,'acc/services.html')  

def redirect_view(request):
    return redirect('acc/stock.html')
    

def createOrder(request):
    form=OrderForm()
    context={'form':form}
    return render(request,'acc/deployment.html',context)



# Create your views here.
