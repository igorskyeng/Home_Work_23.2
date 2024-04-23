from django.contrib import admin
from django.urls import path
from main.views import index
from main.views import contacts
from main.views import home

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('main/<int:pk>/', index),
]
