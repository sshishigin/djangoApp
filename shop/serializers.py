from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from shop.models import Item, UserItemRelation


class ItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'pic', 'available']


class CartItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'pic']


class UserItemRelationSerializer(ModelSerializer):
    class Meta:
        model = UserItemRelation
        fields = ['item']