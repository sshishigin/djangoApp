from django.conf import settings

from shop.models import Item


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, quantity=1):
        if item.id not in self.cart:
            self.cart[item.id] = {'quantity': quantity,
                                  'price': item.price}
            self.save()

    def update_quantity(self, item, quantity):
        if item.id in self.cart:
            self.cart[item.id]['quantity'] = quantity

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, item):
        # Удаление товара из корзины.
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        # получение объектов Item и добавление их в корзину
        items = Item.objects.filter(id__in=self.cart.keys())
        for item in items:
            self.cart[str(item.id)].update(item.to_dict())  # здесь каждый айтем сериализуется в словарь
        for id_, item in self.cart.items():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Подсчет всех товаров в корзине.
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
