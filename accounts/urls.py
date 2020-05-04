from django.contrib.auth import views
from django.urls import path
from .views import registration

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('reg/', registration, name='reg'),
]
