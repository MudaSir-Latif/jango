# from django.shortcuts import render, get_object_or_404,redirect
# from about.models import Product,Cart,CartItem
# from django.core.paginator import Paginator
# from .forms import AddToCartForm


# def shop(request):
#     category = request.GET.get('category', None)
#     if category and category.upper() != 'ALL':
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()

#     paginator = Paginator(products, 8)  
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'shop.html', {'page_obj': page_obj, 'category': category})


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
    
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST, product_id=product_id)
#         if form.is_valid():
#             size = form.cleaned_data['size']
#             colour = form.cleaned_data['colour']
#             quantity = form.cleaned_data['quantity']
            
#             cart, created = Cart.objects.get_or_create(user=request.user)
#             cart_item, created = CartItem.objects.get_or_create(
#                 cart=cart, product=product, size=size, colour=colour,
#                 defaults={'quantity': quantity}
#             )
#             if not created:
#                 cart_item.quantity += quantity
#                 cart_item.save()
            
#             # Update product stock
#             product.stock -= quantity
#             product.save()
            
#             return redirect('cart')  # Redirect to the cart page after adding item
#     else:
#         form = AddToCartForm(product_id=product_id)

#     context = {
#         'product': product,
#         'form': form,
#     }
#     return render(request, 'product.html', context)

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
    
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST, product_id=product_id)
#         if form.is_valid():
#             size = form.cleaned_data['size']
#             colour = form.cleaned_data['colour']
#             quantity = form.cleaned_data['quantity']
            
#             cart, created = Cart.objects.get_or_create(user=request.user)
#             cart_item, created = CartItem.objects.get_or_create(
#                 cart=cart, product=product, size=size, colour=colour,
#                 defaults={'quantity': quantity}
#             )
#             if not created:
#                 cart_item.quantity += quantity
#                 cart_item.save()
            
#             return redirect('cart')  # Redirect to the cart page after adding item
#     else:
#         form = AddToCartForm(product_id=product_id)

#     context = {
#         'product': product,
#         'form': form,
#     }
#     return render(request, 'product.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from about.models import Product, Cart, CartItem
from django.core.paginator import Paginator
from .forms import AddToCartForm

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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST, product_id=product_id)
        if form.is_valid():
            size = form.cleaned_data['size']
            colour = form.cleaned_data['colour']
            quantity = form.cleaned_data['quantity']
            
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product, size=size, colour=colour,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            # Update product stock
            product.stock -= quantity
            product.save()
            
            return redirect('cart')  # Redirect to the cart page after adding item
    else:
        form = AddToCartForm(product_id=product_id)

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST, product_id=product_id)
        if form.is_valid():
            size = form.cleaned_data['size']
            colour = form.cleaned_data['colour']
            quantity = form.cleaned_data['quantity']
            
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product, size=size, colour=colour,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            return redirect('cart')  # Redirect to the cart page after adding item
    else:
        form = AddToCartForm(product_id=product_id)

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product.html', context)
