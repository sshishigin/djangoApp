from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from shop.models import Like
from users.models import CustomUser


class UsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff']


class LikesSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['item']
