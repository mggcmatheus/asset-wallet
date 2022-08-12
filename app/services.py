import requests
from decouple import config
from app.mongodb import PriceTicker
from .models import Ticker

API_KEY = config('ALPHA_VANTAGE_API_KEY')


def get_quote_full(ticker=None):
    ticker = ticker.upper()
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}.SAO&outputsize=full&apikey={API_KEY}'

    r = requests.get(url)
    data = r.json()

    dict_aux = data['Time Series (Daily)'] if 'Time Series (Daily)' in data else None
    if data is not None:
        pt = PriceTicker()

        for i in dict_aux:
            pt.set_price_ticker(ticker.upper(), i, dict_aux[i]['4. close'])


def sync_all_quote():
    tk = Ticker.objects.all()

    for i in tk:
        print(f'Sincronizando ativo: {i.code}')
        get_quote_full(i.code)
