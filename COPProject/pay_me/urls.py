from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='pay_me_view'),
]
