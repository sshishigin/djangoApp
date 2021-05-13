from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.views import CartAPI
from orders.views import OrderAPI, OrderItemViewSet
from shop.views import ItemsViewSet
from users.views import UsersViewSet

router = DefaultRouter()
router.register('api/items', ItemsViewSet)
router.register('api/users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('users/', include('users.urls', namespace='users')),
    path('order/', include('orders.urls', namespace='orders')),
    path('api/orders/', OrderAPI.as_view(), name='orderAPI'),
    path('api/orderItems/', OrderItemViewSet.as_view(), name='orderItemsAPI'),
    path('api/cart/', CartAPI.as_view(), name='cartAPI')
]

urlpatterns += router.urls
