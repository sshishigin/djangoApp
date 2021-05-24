from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from cart.models import Cart
from shop.models import Category, Item
from users.models import CustomUser


class CartApiTestCase(APITestCase):
    def test(self):
        category = Category.objects.create(company='testCaseCompany', in_box=True)
        item1 = Item.objects.create(title='testCaseItem1', price=1111, category=category)
        factory = APIRequestFactory()
        request = factory.get('/api/items/')
        user = CustomUser.objects.create_user('test@heh.rip', 'test123')
        force_authenticate(request, user=user)
        cart = Cart(request)
        cart.add(item=item1, quantity=222)
        cart.save()
        print(cart)
        self.assertEqual(cart)
