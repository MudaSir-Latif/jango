from django.shortcuts import render

def shop(request):
    return render (request,'shop.html')

def product(request):
    return render (request,'product.html')
