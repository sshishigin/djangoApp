from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from shop.models import Item, UserItemRelation


class ItemsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'pic', 'available']


class UserItemRelationSerializer(ModelSerializer):
    class Meta:
        model = UserItemRelation
        fields = ['item']