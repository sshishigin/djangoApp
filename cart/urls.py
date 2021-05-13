from django.urls import path

from cart.views import cart_detail

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
]
