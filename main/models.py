from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    Description = models.TextField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.Description}'

    class Meta:
        verbose_name = 'наименование_категории'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    Description = models.TextField(max_length=100, verbose_name='описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_per_purchase = models.IntegerField(verbose_name='цена_за_покупку')
    created_at = models.DateTimeField(max_length=100, verbose_name='дата_создания_(записи_в_БД)')
    updated_at = models.DateTimeField(max_length=100, verbose_name='дата_последнего_изменения_(записи_в_БД)')
    manufactured_at = models.DateTimeField(verbose_name='дата_производства_продукта')

    def __str__(self):
        return f'{self.name} {self.Description}'

    class Meta:
        verbose_name = 'наименование_продукта'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='student/', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)
