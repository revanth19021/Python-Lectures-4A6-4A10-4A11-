from .views import hai,register,login

from django.urls import path



urlpatterns = [
    path('',hai),
    path('register/',register),
    path('login/',login),
]
