from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

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
    path('order/', include('orders.urls', namespace='orders'))
]

urlpatterns += router.urls
