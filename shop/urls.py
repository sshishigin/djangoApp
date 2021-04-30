from django.urls import path, include
from . import views
##############  URL схемы для главной страницы ##################

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('pruduct/<int:id>', views.item_page, name='item_page'),
    path('new', views.index_w_api),
]