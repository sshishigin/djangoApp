from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import CustomUser
from .forms import CustomUserCreationForm
from orders.models import Order
# Create your views here.

def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("shop:index")
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def show_profile(request):
    UserProfileContext = UserProfile.objects.get(user=request.user)
    UserOrders = Order.objects.filter(user=request.user)
    context = {'user_profile' : UserProfileContext, 'orders' : UserOrders}
    return render(request, 'profile/user_profile.html', context)