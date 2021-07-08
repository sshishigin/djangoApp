import redis
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from rest_framework.generics import get_object_or_404

from shop.models import Item
from shop.serializers import CartItemSerializer


class Cart(object):
    def __init__(self, request=None):
        self.client = redis.Redis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT,
                                  db=0)
        self.user_id = request.user
        if self.user_id != AnonymousUser:
            cart = self.client.hgetall(f'cart:{self.user_id}')
            if cart:
                self.cart = cart
            else:
                self.cart = {}

    def add_item(self, item_id: int, quantity: int):
        self.client.hsetnx(f'cart:{self.user_id}', item_id, quantity)

    def remove_item(self, item_id: int):
        self.client.hdel(f'cart:{self.user_id}', item_id)

    def clear(self):
        self.client.delete(f'cart:{self.user_id}')

    def update_quantity(self, item_id: int, quantity: int):
        self.client.hincrby(f'cart:{self.user_id}', item_id, quantity)

    def __iter__(self):
        for id, quantity in self.cart.items():
            try:
                item_in_cart = CartItemSerializer(get_object_or_404(Item, id=id)).data
            except Http404:
                self.client.hdel(f'cart:{self.user_id}', id)
                continue
            item_in_cart['quantity'] = quantity
            yield item_in_cart
