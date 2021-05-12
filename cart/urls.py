from django.urls import path

from cart.views import CartViewSet, cart_detail #, cart_add, cart_remove, cart_manual_clear

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('api/', CartViewSet.as_view()),
    # path('add/', cart_add, name='cart_add'),
    # path('remove/', cart_remove, name='cart_remove'),
    # path('clear/', cart_manual_clear, name='clear'),
]
