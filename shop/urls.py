from django.urls import path, include
from . import views

# URL схемы для главной страницы
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:item_id>', views.item_page, name='item_page'),
]
