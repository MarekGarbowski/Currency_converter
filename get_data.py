import json
import requests
# https://api.nbp.pl/api/exchangerates/tables/c/today/?format=json
# // kursy sprzedaż i zakupu walut w aktualnych cenach, format json


def get_currency_rates(currency, rate_number):
    try:
        url = f'http://api.nbp.pl/api/' \
              f'exchangerates/rates/c/' \
              f'{currency}/' \
              f'last/{rate_number}/' \
              f'?format=json'
        response = requests.get(url)
    except requests.HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        if response.status_code == 200:
            return json.dumps(response.json(), indent=4, sort_keys=True)
        else:
            print(f'Podana waluta "{currency}: nie jest dostępna')
            input('Press enter...')

