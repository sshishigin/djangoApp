from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'shop'

urlpatterns = [
    path('', cache_page(60*15)(views.index), name='index'),
    path('product/<int:item_id>', views.item_page, name='item_page'),
]
