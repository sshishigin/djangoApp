from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shop.models import Item, Category
from shop.serializers import ItemsSerializer


class ItemApiTestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(company='testCaseCompany', in_box=True)
        item1 = Item.objects.create(title='testCaseItem1', price=1111, category=category)
        item2 = Item.objects.create(title='testCaseItem2', price=2222, category=category)
        url = reverse('item-list')
        print(url)
        response = self.client.get(url)
        serializer_data = ItemsSerializer([item1, item2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class ItemsSerializerTestCase(TestCase):
    def test_serialize(self):
        category = Category.objects.create(company='testCaseCompany', in_box=True)
        book_1 = Item.objects.create(title='testCaseItem1', price=1111, category=category)
        book_2 = Item.objects.create(title='testCaseItem2', price=2222, category=category)
        data = ItemsSerializer([book_1, book_2], many=True).data
        expected = [
            {
                'id': book_1.id,
                'title': book_1.title,
                'price': book_1.price,
                'description': book_1.description,
                'pic': book_1.pic,
                'available': book_1.available
            },
            {
                'id': book_2.id,
                'title': book_2.title,
                'price': book_2.price,
                'description': book_2.description,
                'pic': book_2.pic,
                'available': book_2.available
            }
        ]
        self.assertEqual(expected, data)