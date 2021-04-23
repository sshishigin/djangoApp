from django.urls import path, include
from . import views
app_name= 'users'

urlpatterns = [
    path ('', include('django.contrib.auth.urls')),
    ##страница регистрации
    path('register/', views.register, name='register'),
    path('user/', views.show_profile, name='profile'),
    path('logout', views.logout_, name='logout')
]