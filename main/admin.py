from django.contrib import admin
from main.models import Category
from main.models import Product
from main.models import Version
from blog.models import Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'description')
    list_filter = ('name_category',)
    search_fields = ('name_category', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price_per_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('category', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'slug', 'image_preview', 'date_of_creation',
                    'publication_sign', 'views_count')
    list_filter = ('title',)
    search_fields = ('title', 'body')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'version_number', 'name_version', 'sign_current_version')
    list_filter = ('name_product',)
    search_fields = ('name_product', 'name_version')
