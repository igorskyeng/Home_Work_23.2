# Generated by Django 5.0.4 on 2024-05-05 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 18, 9, 51, 236766), max_length=100, verbose_name='Дата создания'),
        ),
    ]