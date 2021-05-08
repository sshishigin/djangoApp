from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from cart.views import cart_add
from shop.views import ItemsViewSet
from users.views import UsersViewSet

router = DefaultRouter()
router.register('api/items', ItemsViewSet)
router.register('api/users', UsersViewSet)
# router.register('api/cart/add/<int:item_id>/', cart_add)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('users/', include('users.urls', namespace='users')),
    path('order/', include('orders.urls', namespace='orders'))
]

urlpatterns += router.urls
