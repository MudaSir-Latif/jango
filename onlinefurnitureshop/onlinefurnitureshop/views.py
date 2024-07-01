from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# def home(request):
#     context = {
#         'range': range(12)  # Pass the range to the context
#     }    
#     return render(request,'home.html',context)

from about.models import Product

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html',context)
        

# @login_required
def checkout(request):
    return render(request,'checkout.html')