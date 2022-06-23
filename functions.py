import requests
import os
from urllib.request import urlopen
import json


def get_currency_rates(currency, rate_number, table):
    try:
        url = f'http://api.nbp.pl/api/' \
              f'exchangerates/rates/{table}/' \
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
            raw_data = response.json()
            return raw_data
        else:
            print(f'The given currency "{currency}": is not available')
            input('Press enter...')


def chosen_currency_status(currency, rate_number):
    data = get_currency_rates(currency, rate_number, "c")
    currency = str(data['currency']).upper()
    currency_ask = data['rates'][0]['ask']
    currency_bid = data['rates'][0]['bid']
    data = f'\n' \
           f'The currency: {currency} in: \n' \
           f'\n' \
           f'sale is for: {currency_ask} PLN, \n' \
           f'\n' \
           f'purchase for: {currency_bid} PLN' \
           f'\n'
    return data


def get_currencies_table():
    try:
        url = "http://api.nbp.pl/api/exchangerates/tables/a/today/?format=json"
        response = urlopen(url)
        data_json = json.loads(response.read())
    except requests.HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        y = 0
        for word in data_json:
            for x in word.values():
                y += 1
                if y == 4:
                    for a in x:
                        print(f'Currency: {a["currency"]}, code {a["code"]}, mid price is: {a["mid"]} PLN')
    input('Press enter...')


def ask_value(currency, amount):
    data = get_currency_rates(currency, 1, "c")
    currency_ask = amount * data['rates'][0]['ask']
    print(currency_ask)
    input('Press enter...')


def bid_value(currency, amount):
    data = get_currency_rates(currency, 1, "c")
    currency_bid = amount * data['rates'][0]['bid']
    print(currency_bid)
    input('Press enter...')


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
