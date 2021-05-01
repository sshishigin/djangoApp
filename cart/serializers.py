from rest_framework.serializers import HyperlinkedModelSerializer
from cart.models import Cart


class CartSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'items']
