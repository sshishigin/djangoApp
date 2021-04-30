from django.shortcuts import render, get_object_or_404
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item
from cart.forms import CartAddProductForm
from shop.serializers import IndexSerializer


# Create your views here.


def index(request):
    ###список товаров###
    items = Item.objects.filter(available=True).order_by('price')
    context = {'items': items}
    return render(request, 'shop/index.html', context)


def item_page(request, id):
    item_on_page = get_object_or_404(Item, id=id, available=True)
    context = {'item': item_on_page,
               'cart_product_form': CartAddProductForm()}
    return render(request, 'templates/shop/item_page.html', context)


def index_w_api(request):
    return render(request, 'shop/new_index.html')


class shop_api(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = IndexSerializer
    filter_backens = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['title', 'company']
    ordering_fields = ['price']
