from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .permissions import IsOwner
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer, UserRegistrationSerializer


class CustomTokenObtain(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        response_user = JSONRenderer().render(ReadOnlyUserSerializer(User.objects.get_by_natural_key(user)).data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response_user})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReadOnlyUserSerializer
        if self.action == 'create':
            return UserRegistrationSerializer
        return WriteOnlyUserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsOwner()]
        if self.action in ['list', 'destroy']:
            return [IsAdminUser()]
        else:
            return [AllowAny()]