from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    #slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержание')
    #image_preview = models.ImageField(upload_to='product/', **NULLABLE)
    #date_of_creation = models.DateTimeField(max_length=100, verbose_name='Дата создания')
    #publication_sign = models.BooleanField(verbose_name='Публикации')
    #number_of_views = models.IntegerField(verbose_name='Количество просмотров')
    #views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
