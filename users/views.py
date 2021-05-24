from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .forms import CustomUserCreationForm
from orders.models import Order
from .serializers import UsersSerializer


def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("shop:index")
    return render(request, 'registration/register.html', {'form': form})


def show_profile(request):
    return render(request, 'profile/user_profile.html')


def logout_(request):
    logout(request)
    return redirect("shop:index")


class UsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

