from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('buy/<int:item_id>/', views.cart_buy, name='cart_buy'),
    path('clear/', views.cart_manual_clear, name='clear')
    # path('update/<int:item_id>/', views.cart_update_quantity, name='cart_update_quantity'),
]