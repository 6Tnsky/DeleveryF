
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('orders/', views.orders, name='orders'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
]