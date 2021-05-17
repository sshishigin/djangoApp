from django.shortcuts import render, get_object_or_404
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from users.serializers import LikesSerializer
from .models import Item, Like
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


class LikeAPI(APIView):
    def get(self, request):
        serializer = LikesSerializer(
            Like.objects.filter(user=request.user),
            many=True
        )
        return Response(data=serializer.data)

    def post(self, request):
        like = Like.objects.get_or_create(user=request.user, item=get_object_or_404(Item, id=request.data['itemId']))
        like.save()
        return Response('Liked', status=200)

    def patch(self, request):
        like = Like.objects.get(user=request.user, item=get_object_or_404(Item, id=request.data['itemId']))
        like.delete()
        return Response('Like deleted', status=200)
