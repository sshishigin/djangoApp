from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', cache_page(60*15)(views.show_profile), name='profile'),
]
