from django.shortcuts import render, get_object_or_404
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item
from cart.forms import CartAddProductForm
from shop.serializers import ItemsSerializer


# Create your views here.


def index(request):
    items = Item.objects.filter(available=True).order_by('price')
    context = {'items': items}
    return render(request, 'shop/index.html', context)


def index_w_api(request):
    return render(request, 'shop/new_index.html')


def item_page(request, item_id):
    item_on_page = get_object_or_404(Item, id=item_id, available=True)
    context = {'item': item_on_page,
               'cart_product_form': CartAddProductForm()}
    return render(request, 'templates/shop/item_page.html', context)


class ItemsViewSet(ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price', 'available']
    search_fields = ['title']
    ordering_fields = ['price']
