from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Item
from .forms import CartAddProductForm
from .models import Cart
# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'cart': cart,
                    'cart_product_form': cart_product_form})

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,  
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_buy(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.add(item=product)
    return redirect('cart:cart_detail')

def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_manual_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')