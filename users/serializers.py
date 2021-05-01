from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import CustomUser


class UsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff']
