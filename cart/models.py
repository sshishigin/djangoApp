import redis

from django.conf import settings
from rest_framework.generics import get_object_or_404

from shop.models import Item
from shop.serializers import CartItemSerializer


class Cart(object):
    def __init__(self, request=None):
        self.client = redis.Redis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT,
                                  db=0)
        self.user = request.user.get_username()
        cart = self.client.hgetall(f'cart:{self.user}')
        self.cart = cart

    def add_item(self, item_id, quantity):
        self.client.hsetnx(f'cart:{self.user}', item_id, quantity)

    def remove_item(self, item_id):
        self.client.hdel(f'cart:{self.user}', item_id)

    def clear(self):
        self.client.delete(f'cart:{self.user}')

    def update_quantity(self, item_id, quantity):
        self.client.hincrby(f'cart:{self.user}', item_id, quantity)

    def __iter__(self):
        for key, value in self.cart.items():
            item_in_cart = CartItemSerializer(get_object_or_404(Item, id=key)).data
            item_in_cart['quantity'] = value
            yield item_in_cart
