from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import profile

app_name = 'payme'

urlpatterns = [
    # Define your application's URLs here
    path('', views.home, name='home'),  # Define a root URL pattern
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	# path('profile/', profile, name='profile'),
    path('profile/', views.profile, name='profile'),
	path('generate/', views.generate_url, name='generate_url'),
    # path('<str:random_url>/', views.generate_url, name='generate_url'),
	path('delete/<int:pk>/', views.delete_link, name='delete_link'),
	path('<str:random_url>/', views.process_url, name='process_url'),
    # Add more URL patterns as necessary
]