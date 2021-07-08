from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'address', 'postal_code', 'city', 'created', 'paid']


class OrderPostSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'price', 'quantity']