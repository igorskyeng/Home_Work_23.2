from django.contrib import admin
from django.urls import path

from main.apps import MainConfig
from main.views import (contacts, ProductListView, ProductDetailtView, ContactPageView, ProductCreateView,
                        ProductUpdateView, ProductDeleteView)

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactPageView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailtView.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product')
]
