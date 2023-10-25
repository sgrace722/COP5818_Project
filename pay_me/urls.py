from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='pay_me_view'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view')
]
