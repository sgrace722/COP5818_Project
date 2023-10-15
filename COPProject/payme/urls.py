from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'payme'

urlpatterns = [
    # Define your application's URLs here
    path('', views.home, name='home'),  # Define a root URL pattern
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('profile/', views.profile, name='profile'),
    # Add more URL patterns as necessary
]