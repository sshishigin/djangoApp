from django.shortcuts import render, get_object_or_404
from .models import Item
from cart.forms import CartAddProductForm
# Create your views here.


def index(request):
    ###список товаров###
    items = Item.objects.filter(available=True).order_by('price')
    context = {'items': items}
    return render(request, 'shop/index.html', context)

def item_page(request, id):
    item_on_page = get_object_or_404(Item, id=id, available=True)
    context = {'item':item_on_page,
            'cart_product_form': CartAddProductForm()}
    return render(request, 'templates/shop/item_page.html', context)