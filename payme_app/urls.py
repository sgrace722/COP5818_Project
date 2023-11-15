# myapp/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('payment_records/<str:url>/', views.payment_records_view, name='payment_records_view'),
    path('register/', views.register_view, name='register_view'),
]
