from django.shortcuts import redirect, render
from store.models import Product
from .import models

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request , product_id):
    product = Product.objects.get(id = product_id)

    try:
        cart = models.Cart.objects.get(cart_id = _cart_id(request))
    except models.Cart.DoesNotExist:
        cart = models.Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = models.CartItem.objects.get(product = product , cart = cart)
        cart_item.quantity +=1
        cart_item.save()
    except models.CartItem.DoesNotExist:
        cart_item = models.CartItem.objects.create(
            product = product , 
            quantity = 1 , 
            cart = cart
        )
        cart_item.save()
    return redirect('cart')
    


def cart(request):
    return render(request , 'store/cart.html')