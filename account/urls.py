from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswardResetView
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='text-align:center'>User App<h1>")

urlpatterns = [
    
    path('', index),
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('change-password/', UserChangePasswordView.as_view(), name="change-password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name="send-reset-password-email"),
    path('reset-passward/<uid>/<token>/', UserPasswardResetView.as_view(), name="reset-passward"),
]
