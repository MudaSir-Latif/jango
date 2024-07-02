from django.shortcuts import render
from about.models import Cart

# def cart(request):
#     return render(request,'cart.html')


def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        
        for item in cart_items:
            item.subtotal = item.product.price * item.quantity
        
        context = {
            'cart': cart,
            'cart_items': cart_items,
        }
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
        context = {
            'cart': cart,
            'cart_items': cart_items,
        }
    
    return render(request, 'cart.html', context)
