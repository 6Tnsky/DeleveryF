from django.test import TestCase

# Create your tests here.

from .models import Product  # Импортируем вашу модель товаров

class ProductTestCase(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        Product.objects.create(name="Розы", price=1000)
        Product.objects.create(name="Тюльпаны", price=500)

    def test_product_list(self):
        # Проверяем, что товары корректно добавлены в базу
        products = Product.objects.all()
        self.assertEqual(products[0].name, "Розы")
        self.assertEqual(products[1].price, 500)
