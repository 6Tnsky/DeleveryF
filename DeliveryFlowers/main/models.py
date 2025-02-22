from django.db import models
from django.contrib.auth.models import User  # Импорт модели User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/')  # Изображения товаров

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'


# Модель для заказов
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    products = models.ManyToManyField('Product')  # Связь с продуктами
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'