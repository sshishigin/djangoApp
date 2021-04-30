from rest_framework.serializers import ModelSerializer
from shop.models import Item


class IndexSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'price', 'description', 'pic']
