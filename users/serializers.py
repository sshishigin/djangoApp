from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from shop.models import UserItemRelation
from users.models import CustomUser


class UsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff']

