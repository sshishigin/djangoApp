from rest_framework.serializers import HyperlinkedModelSerializer
from shop.models import Item


class ItemsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'description', 'pic', 'available']
