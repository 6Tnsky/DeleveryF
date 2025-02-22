from django.contrib import admin
from .models import Product, Order
# Register your models here.

# Настройка админки для модели Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поиск по названию продукта
    list_filter = ('price',)  # Фильтр по цене
    ordering = ('name',)  # Сортировка по названию



# Настройка админки для модели Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'product_list')  # Поля, которые будут отображаться в списке
    list_filter = ('created_at',)  # Фильтр по дате создания
    search_fields = ('user__username',)  # Поиск по имени пользователя
    autocomplete_fields = ('user', 'products')  # Автозаполнение для пользователей и продуктов
    date_hierarchy = 'created_at'  # Добавление иерархии по дате

    def product_list(self, obj):
        """Отображение списка продуктов в заказе."""
        return ", ".join([product.name for product in obj.products.all()])
    product_list.short_description = "Продукты"  # Заголовок колонки


# Регистрируем модели с кастомными настройками
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


