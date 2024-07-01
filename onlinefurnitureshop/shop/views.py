from django.shortcuts import render, get_object_or_404
from about.models import Product
from django.core.paginator import Paginator

# def shop(request):
#     # return render (request,'shop.html')
#     category = request.GET.get('category', None)
#     if category:
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()

#     paginator = Paginator(products, 1)  # Show 10 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'shop.html', {'page_obj': page_obj})
#     # return render(request, 'shop.html', {'products': products})


def shop(request):
    category = request.GET.get('category', None)
    if category and category.upper() != 'ALL':
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop.html', {'page_obj': page_obj, 'category': category})


# def product(request):
#     return render (request,'product.html')

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)