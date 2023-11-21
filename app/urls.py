from django.urls import path
from . import views
from .views import get_binance_prices
from .views import list_cryptos

urlpatterns = [
    path('', views.index, name='index'),
    path('list_programmers/', views.list_programmers, name='list_programmers'),
    path('list_cryptos/', views.list_cryptos, name='list_cryptos'),
    path('get_binance_crypto_info/<str:symbol>/', views.get_binance_crypto_info, name='get_binance_crypto_info'),
    path('get_binance_prices/', views.getBinancePrices, name='get_binance_prices')

]
