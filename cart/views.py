from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CartSerializer
from shop.models import Item
from .forms import CartAddProductForm


from .models import Cart


class CartViewSet(APIView):
    serializer_class = CartSerializer

    def get(self, request, format=None):
        cart = Cart(request)
        return Response(cart)


@api_view()
def cart_detail(request):
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'cart_product_form': cart_product_form})


@api_view(['POST'])
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    print(request.data)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print("here", cd)
        cart.add(item=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        try:
            cart.add(
                item=item,
                quantity=request.data['data']['quantity'],
                update_quantity = True
            )
        except:
            print('Ну пиздец')
    return redirect('cart:cart_detail')


@api_view()
def cart_buy(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.add(item=product)
    return redirect('cart:cart_detail')


@api_view()
def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@api_view()
def cart_manual_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
