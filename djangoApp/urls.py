from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.views import CartAPI
from djangoApp.routers import DefaultRouterWithSimpleViews
from orders.views import OrderAPI, OrderItemViewSet
from shop.views import ItemsViewSet, LikeAPI
from users.views import UsersViewSet

router = DefaultRouter()
router.register('api/items', ItemsViewSet)
router.register('api/users', UsersViewSet)
router.register('api/orderItems', OrderItemViewSet)
extra_router = DefaultRouterWithSimpleViews()

extra_router.register('api/cart', CartAPI, 'cartAPI')
extra_router.register('api/order', OrderAPI, 'orderAPI')
extra_router.register('api/like', LikeAPI, 'likeAPI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('users/', include('users.urls', namespace='user')),
    path('order/', include('orders.urls', namespace='orders')),
]

urlpatterns += router.urls
urlpatterns += extra_router.urls
