from rest_framework.serializers import ModelSerializer

from users.models import User


class ReadOnlyUserSerializer(ModelSerializer):
    # Serializer для чтения данных юзера
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'last_login', 'is_superuser', 'first_name', 'last_name']


class UserRegistrationSerializer(ModelSerializer):
    # Serializer для регистрации юзера
    class Meta:
        model = User
        fields = ['email', "password", 'is_active', 'last_login', 'is_superuser', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class WriteOnlyUserSerializer(ModelSerializer):
    # Serializer для обновления
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'first_name', 'last_name']


