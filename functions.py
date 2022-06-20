import requests
import os


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
            raw_data = response.json()
            return raw_data
        else:
            print(f'The given currency "{currency}": is not available')
            input('Press enter...')


def chosen_currency_status(currency, rate_number):
    data = get_currency_rates(currency, rate_number)
    currency = str(data['currency']).upper()
    currency_ask = data['rates'][0]['ask']
    currency_bid = data['rates'][0]['bid']
    # print(data)
    data = f'\n' \
           f'The currency: {currency} in: \n' \
           f'\n' \
           f'sale is for: {currency_ask} PLN, \n' \
           f'\n' \
           f'purchase for: {currency_bid} PLN' \
           f'\n'
    return data


def ask_value(currency):
    data = get_currency_rates(currency, 1)
    currency_ask = data['rates'][0]['ask']
    return currency_ask


def bid_value(currency):
    data = get_currency_rates(currency, 1)
    currency_ask = data['rates'][0]['bid']
    return currency_ask


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
