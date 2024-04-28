from django.contrib import admin
from django.urls import path

from main.apps import MainConfig
from main.views import contacts, ProductListView, ProductDetailtView, ContactPageView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailtView.as_view(), name='view_product'),
]
