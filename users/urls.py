from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, PasswordRecoveryView, LoginView#, email_verification

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    #path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
]
