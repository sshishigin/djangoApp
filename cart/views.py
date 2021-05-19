from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Item
from .models import Cart

# 'api/cart'


class CartAPI(APIView):

    def get(self, request):
        return Response(Cart(request), status=200)

    def post(self, request):
        try:
            Cart(request).add(
                item=get_object_or_404(Item, id=request.data['itemId']),
                quantity=request.data['quantity'],
            )
            return Response(status=202)
        except KeyError:
            return Response('Bad request, itemId & quantity required')

    def put(self, request):
        print(request.data)
        if request.data['itemIdList']:
            item_id_list = request.data['itemIdList']
            for item_id in item_id_list:
                Cart(request).remove(get_object_or_404(Item, id=item_id))
            return Response("Item(s) deleted", status=200)
        else:
            return Response('Bad request, проверьте id')

    def patch(self, request):
        if request.data['quantity'] and request.data['itemId']:
            Cart.updateItemQuantity(
                item=get_object_or_404(Item, id=request.data['itemId']),
                quantity=request.data['quantity']
            )
            return Response('Quantity updated', status=200)
        else:
            return Response('Bad request(quantity or itemId is missing', status=204)








def cart_detail(request):
    return render(request, 'cart/cartDetail.html')
