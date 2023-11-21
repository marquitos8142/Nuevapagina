from django.http import JsonResponse
from django.shortcuts import render
from .models import Programmer
from .binance_api import BinanceAPI, BinanceAPIException
from requests.exceptions import RequestException

# Claves de API (podrías moverlas a settings.py)
API_KEY = 'Hcv87Vc7dp9sIafgxkf1ZakrtRwA1cKrVOTMONNLWFZOdGtVZgjpTZZlsE2AQDl7'
API_SECRET = '0zEkYxTOJq54hxY1Xem4wgtzlufUlR5KWwu8igCMpDLwyFwQ2xnXIbG3Ezf1hehf'

def get_binance_prices(request):
    try:
        binance_api = BinanceAPI(API_KEY, API_SECRET)
        symbol_price = binance_api.get_symbol_price('BTCUSDT')
        return JsonResponse({'price': symbol_price})
    except (BinanceAPIException, RequestException) as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def getBinancePrices(request):
    try:
        binance_api = BinanceAPI(API_KEY, API_SECRET)
        symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']  # Agrega los símbolos que desees obtener
        prices = binance_api.get_multiple_symbol_prices(symbols)
        return JsonResponse({'prices': prices})
    except BinanceAPIException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': f"Error inesperado: {str(e)}"}, status=500)
    
from django.shortcuts import render
from .binance_api import BinanceAPI

def get_binance_crypto_info(request, symbol):
    try:
        binance_api = BinanceAPI(API_KEY, API_SECRET)
        crypto_info = binance_api.get_crypto_info(symbol)
        return JsonResponse({'info': crypto_info})
    except BinanceAPIException as e:
        return JsonResponse({'error': str(e)}, status=500)

def list_cryptos(request):
    try:
        # Agrega tu clave API y secreto aquí
        api_key = 'TU_API_KEY'
        api_secret = 'TU_API_SECRET'

        binance_api = BinanceAPI(api_key, api_secret)

        # Agrega los símbolos de criptomonedas que desees obtener
        symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'DOTUSDT', 'SOLUSDT']
        cryptos_info = binance_api.get_multiple_crypto_info(symbols)

        # Formatea la información para pasarla al template
        crypto_data = [
            {
                "name": "Bitcoin",
                "country": "Cryptoland",
                "symbol": "BTCUSDT",
                "price": cryptos_info['BTCUSDT']['price']
            },
            {
                "name": "Ethereum",
                "country": "Cryptoland",
                "symbol": "ETHUSDT",
                "price": cryptos_info['ETHUSDT']['price']
            },
            {
                "name": "Binance Coin",
                "country": "Cryptoland",
                "symbol": "BNBUSDT",
                "price": cryptos_info['BNBUSDT']['price']
            },
            {
                "name": "Polkadot",
                "country": "Cryptoland",    
                "symbol": "DOTUSDT",
                "price": cryptos_info['DOTUSDT']['price']
            },
            {
                "name": "Solana",
                "country": "Cryptoland",
                "symbol": "SOLUSDT",
                "price": cryptos_info['SOLUSDT']['price']
            },
            # Agrega más criptomonedas según sea necesario
        ]

        return JsonResponse({'cryptos': crypto_data})
    except Exception as e:
        return null



def obtener_precio_binance(request):
    try:
        binance_api = BinanceAPI(API_KEY, API_SECRET)
        symbol = 'BTCUSDT'
        precio = binance_api.get_symbol_price(symbol)
        return render(request, 'tu_template.html', {'precio': precio})
    except BinanceAPIException as e:
        # Manejar la excepción específica de BinanceAPI
        return render(request, 'error.html', {'error_message': str(e)})
    except RequestException as e:
        # Manejar la excepción específica de RequestException
        return render(request, 'error.html', {'error_message': str(e)})

def index(request):
    return render(request, 'index.html')

def list_programmers(_request):
    programmers = list(Programmer.objects.values())
    data = {'programmers': programmers}
    return JsonResponse(data)