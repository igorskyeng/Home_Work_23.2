# Generated by Django 5.0.4 on 2024-05-05 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'permissions': (('cancellation_of_publication', 'отмена публикации'), ('change_Description', 'изменить описание'), ('change_category', 'изменить категорию')), 'verbose_name': 'Название продукта', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 17, 31, 9, 141822), max_length=100, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 17, 31, 9, 141822), max_length=100, verbose_name='Дата последнего изменения'),
        ),
    ]
