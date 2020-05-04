from django.contrib.auth import views
from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index, name='/'),
    path('create/', create, name='battle/create/'),
]

