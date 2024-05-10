from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (ProductListView, ProductDetailtView, ContactPageView, ProductCreateView,
                        ProductUpdateView, ProductDeleteView, CategoryListView)

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('contact/', ContactPageView.as_view(), name='contacts'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailtView.as_view()), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product')
]
