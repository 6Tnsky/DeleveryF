from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from .models import Product, Order
from .bot import send_order_to_telegram  # Импортируем функцию отправки в Telegram

# Create your views here.
def index(request):
    products  = Product.objects.all()
    return render(request,'main/index.html', {'products': products})

def orders(request):
    products = Product.objects.all()
    return render(request, 'main/orders.html', {'products': products})

def login_view(request):
    return render(request,'main/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('orders')  # Если пользователь уже авторизован, перенаправляем на страницу заказов

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('orders')  # Перенаправляем на страницу заказов
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('orders')  # Если пользователь уже авторизован, перенаправляем на страницу заказов

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('orders')  # Перенаправляем на страницу заказов
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу входа

@login_required
def orders_view(request):
    products = Product.objects.all()
    return render(request, 'main/orders.html', {'products': products})

@login_required
def create_order(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')  # Получаем выбранные ID продуктов
        if product_ids:  # Проверяем, что хотя бы один продукт выбран
            # Создаем новый заказ для текущего пользователя
            order = Order.objects.create(user=request.user)
            # Добавляем выбранные продукты в заказ
            products = Product.objects.filter(id__in=product_ids)
            order.products.set(products)
            order.save()
            # Отправляем информацию о заказе в Telegram
            send_order_to_telegram(order)
            return render(request, 'main/order_success.html', {'order': order})  # Перенаправляем на страницу успеха
        else:
            # Если ничего не выбрано, просто остаемся на текущей странице
            return render(request, 'main/orders.html', {
                'products': Product.objects.all(),
                'error': 'Выберите хотя бы один продукт.'
            })


def order_success(request):
    return render(request, 'main/order_success.html')