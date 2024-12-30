# классы бота
import requests
import json
from config import keys, YOUR_API_KEY

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        # Запрос к API ExchangeRate-API
        r = requests.get(f'https://v6.exchangerate-api.com/v6/{YOUR_API_KEY}/latest/USD')
        data = json.loads(r.content)

        # Проверка ошибок в ответе API
        if "error" in data:
            raise ConvertionException(f'Ошибка от API: {data["error-type"]}')
        if "conversion_rates" not in data:
            raise ConvertionException('Не удалось получить курсы валют.')

        # Извлечение курсов валют
        conversion_rates = data["conversion_rates"]
        if quote_ticker not in conversion_rates or base_ticker not in conversion_rates:
            raise ConvertionException(f'Не удалось получить данные для валюты.')

        # Расчёт курса
        quote_rate = conversion_rates[quote_ticker]
        base_rate = conversion_rates[base_ticker]
        rate = base_rate / quote_rate
        total_base = rate * amount

        return round(total_base, 2)





