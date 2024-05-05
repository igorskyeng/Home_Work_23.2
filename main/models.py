from datetime import datetime

from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Название продукта')
    Description = models.TextField(max_length=100, verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price_per_purchase = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(default=datetime.now(), max_length=100, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=datetime.now(), max_length=100, verbose_name='Дата последнего изменения')
    publication_sign = models.BooleanField(default=True, verbose_name='Публикация')
    trader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Продавец', **NULLABLE)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Название продукта'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

        permissions = (
            (
                'cancellation_of_publication',
                'отмена публикации'
            ),
            (
                'change_Description',
                'изменить описание'
            ),
            (
                'change_category',
                'изменить категорию'
            ),
        )


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='student/', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('last_name',)


class Version(models.Model):
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название продукта')
    version_number = models.IntegerField(default=1.0, verbose_name='Версия')
    name_version = models.CharField(max_length=100, verbose_name='Название версии')
    sign_current_version = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return str(self.name_product)

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продуктов'
        ordering = ('id',)
