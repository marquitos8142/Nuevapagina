from binance.client import Client
from binance.exceptions import BinanceAPIException

# Claves de API (podrías moverlas a settings.py)
API_KEY = 'Hcv87Vc7dp9sIafgxkf1ZakrtRwA1cKrVOTMONNLWFZOdGtVZgjpTZZlsE2AQDl7'
API_SECRET = '0zEkYxTOJq54hxY1Xem4wgtzlufUlR5KWwu8igCMpDLwyFwQ2xnXIbG3Ezf1hehf'

class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_symbol_price(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except BinanceAPIException as e:
            raise BinanceAPIException(f"Error en Binance API: {str(e)}")
        except Exception as e:
            raise BinanceAPIException(f"Error inesperado: {str(e)}")

    def get_multiple_symbol_prices(self, symbols):
        prices = {}
        try:
            for symbol in symbols:
                ticker = self.client.get_symbol_ticker(symbol=symbol)
                prices[symbol] = float(ticker['price'])
            return prices
        except BinanceAPIException as e:
            raise BinanceAPIException(f"Error en Binance API: {str(e)}")
        except Exception as e:
            raise BinanceAPIException(f"Error inesperado: {str(e)}")
        
    def get_crypto_info(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return {
                "symbol": symbol,
                "price": float(ticker['price'])
            }
        except BinanceAPIException as e:
            raise BinanceAPIException(f"Error en Binance API: {str(e)}")
        except Exception as e:
            raise BinanceAPIException(f"Error inesperado: {str(e)}")

    def get_multiple_crypto_info(self, symbols):
        cryptos_info = {}
        for symbol in symbols:
            cryptos_info[symbol] = self.get_crypto_info(symbol)
        return cryptos_info

