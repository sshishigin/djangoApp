from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Item
from .models import Cart


class CartViewSet(APIView):
    def get(self, request, format=None):
        return Response(Cart(request), status=200)


def cart_detail(request):
    return render(request, 'cart/cartDetail.html')


@api_view(['POST'])
def cart_add(request):
    item_id = request.data['item_id']
    quantity = request.data['quantity']
    Cart(request).add(
        item=get_object_or_404(Item, id=item_id),
        quantity=quantity,
        update_quantity=True
    )
    return Response(status=202)


@api_view(['POST'])
def cart_remove(request):
    item_id = request.data['item_id']
    Cart(request).remove(get_object_or_404(Item, id=item_id))
    return Response(status=200)


@api_view(['POST'])
def cart_manual_clear(request):
    Cart(request).clear()
    return Response(status=200)
