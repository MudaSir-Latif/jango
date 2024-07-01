from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from about.models import Product




def home(request):
    discounted_products = Product.objects.exclude(discount__isnull=True).exclude(discount__exact='')
    low_stock_products = Product.objects.filter(stock__lt=10)
    context = {
        'products': discounted_products,
        'hot_products': low_stock_products
    }
    return render(request, 'home.html',context)
        

# @login_required
def checkout(request):
    return render(request,'checkout.html')