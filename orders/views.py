from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Item
from .models import Order
from .models import OrderItem
from cart.models import Cart
from .serializers import OrderSerializer, OrderPostSerializer, OrderItemSerializer


class OrderAPI(APIView):
    def post(self, request):
        cart = Cart(request)
        serializer = OrderPostSerializer()
        order = serializer.create(validated_data=request.data['order'])
        if cart:
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=get_object_or_404(Item, id=item['id']),
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return Response(status=200)
        return Response(status=203)

    def get(self, request, format=None):
        serializer = OrderSerializer(
            Order.objects.filter(user=request.user), many=True
        )
        return Response(serializer.data)


class OrderItemViewSet(APIView):
    def get(self, request):
        serializer = OrderItemSerializer(
            OrderItem.objects.filter(
                order=get_object_or_404(Order, id=request.data['orderId'])
            ),
            many=True
        )
        return Response(serializer.data)
