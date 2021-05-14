from django.urls import path

from orders.views import make_order_view

app_name = 'orders'

urlpatterns = [
    path('', make_order_view)
]
