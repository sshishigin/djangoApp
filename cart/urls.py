from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart import views
from cart.views import CartViewSet

router = DefaultRouter()
router.register('api/', CartViewSet, basename='cart-api')
app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.cart_add, name='cart_add'),
    # path('api/', CartViewSet.as_view()),
    path('remove/', views.cart_remove, name='cart_remove'),
    path('clear/', views.cart_manual_clear, name='clear'),
]
urlpatterns += router.urls
print(router.urls)
