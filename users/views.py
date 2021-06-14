from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .permissions import IsOwner
from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer, UserRegistrationSerializer


def show_profile(request):
    return render(request, 'profile/user_profile.html')


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()

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