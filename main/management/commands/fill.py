from django.core.management import BaseCommand
import json
from main.models import Category
from main.models import Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():

        list_of_categories = ''

        with open('categories.json', 'r', encoding='UTF=8') as file:
            for line in file:
                list_of_categories += line

        list_of_categories = json.loads(list_of_categories)
        file.close()

        return list_of_categories

    @staticmethod
    def json_read_products():

        list_of_products = ''

        with open('products.json', 'r', encoding='UTF=8') as file:
            for line in file:
                list_of_products += line

        list_of_products = json.loads(list_of_products)
        file.close()

        return list_of_products

    def handle(self, *args, **options):

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name_category=category['fields']['name_category'],
                         description=category['fields']['description'])
            )

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name_product=product['fields']['name_product'],
                        description=product['fields']['description'],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=category['pk']),
                        price_per_purchase=product['fields']['price_per_purchase'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )
