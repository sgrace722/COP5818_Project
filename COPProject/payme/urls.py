from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('url', views.url_page, name='url_page')
]
