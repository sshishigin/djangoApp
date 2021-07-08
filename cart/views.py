from audioop import error

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart


class CartAPI(APIView):
    def get(self, request):
        try:
            return Response(Cart(request), status.HTTP_200_OK)
        except error as e:
            return Response('BadRequest', status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            Cart(request).add_item(
                item_id=request.data['itemId'],
                quantity=request.data['quantity'],
            )
            return Response(status.HTTP_202_ACCEPTED)
        except KeyError:
            return Response('Bad request, itemId & quantity required')

    def put(self, request):
        if request.data['itemIdList']:
            item_id_list = request.data['itemIdList']
            for item_id in item_id_list:
                Cart(request).remove_item(item_id)
            return Response("Item(s) deleted", status.HTTP_202_ACCEPTED)
        else:
            return Response('Bad request, проверьте id')

    def patch(self, request):
        if request.data['quantity'] and request.data['itemId']:
            Cart.update_quantity(
                item_id=request.data['itemId'],
                quantity=request.data['quantity']
            )
            return Response('Quantity updated', status.HTTP_200_OK)
        else:
            return Response('Bad request(quantity or itemId is missing', status=204)

    def delete(self, request):
        Cart(request).clear()
        return Response("Cart cleared", status.HTTP_204_NO_CONTENT)