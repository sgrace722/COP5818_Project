from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # Define a root URL pattern
	path('all_users/', views.all_users, name='all_users'),  # URL for displaying all users
]