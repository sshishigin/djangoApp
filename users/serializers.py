from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class ReadOnlyUserSerializer(ModelSerializer):
    # Serializer для чтения данных юзера
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser']


class UserRegistrationSerializer(ModelSerializer):
    # Serializer для регистрации юзера
    class Meta:
        model = CustomUser
        fields = ['email', "password", 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class WriteOnlyUserSerializer(ModelSerializer):
    # Serializer для обновления
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


