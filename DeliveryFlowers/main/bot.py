import requests

# Токен вашего Telegram-бота
TELEGRAM_BOT_TOKEN = '7633865260:AAFg1F1uJYgYu4W7cVGTd-dr4V5Z0rAu1Qs'
# ID чата, куда будут отправляться сообщения (можно использовать ваш Telegram ID)
TELEGRAM_CHAT_ID = '319570892'

def send_order_to_telegram(order):
    """
    Отправляет информацию о заказе в Telegram.
    """
    # Формируем текст сообщения
    message = f"Новый заказ!\n\n"
    message += f"Пользователь: {order.user.username} ({order.user.email})\n"
    message += f"Дата заказа: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
    message += f"Продукты:\n"

    for product in order.products.all():
        message += f"- {product.name} (Цена: {product.price} руб.)\n"

    total_price = sum(product.price for product in order.products.all())
    message += f"\nОбщая стоимость: {total_price} руб."

    # URL для отправки сообщения
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    # Параметры запроса
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # Используем HTML для форматирования текста
    }

    # Отправляем POST-запрос
    response = requests.post(url, data=payload)

    # Проверяем успешность запроса
    if response.status_code == 200:
        print("Сообщение успешно отправлено в Telegram.")
    else:
        print(f"Ошибка отправки сообщения: {response.text}")