from django.shortcuts import render
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item
from shop.serializers import ItemsSerializer


def index(request):
    return render(request, 'shop/index.html')


def item_page(request, item_id):
    return render(request, 'shop/item_page.html', {'item_id': item_id})


class ItemsViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'price', 'available']
    search_fields = ['title', 'description']
    ordering_fields = ['price']
