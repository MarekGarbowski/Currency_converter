import requests
# https://api.nbp.pl/api/exchangerates/tables/c/today/?format=json
# kursy sprzedaż i zakupu walut w aktualnych cenach, format json


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
            currency = raw_data['currency']
            currency_ask = raw_data['rates'][0]['ask']
            currency_bid = raw_data['rates'][0]['bid']
            print(f'The currency: {currency} in sale is for: {currency_ask} '
                  f'PLN, and in purhcase for: {currency_bid} PLN')
        else:
            print(f'The given currency "{currency}: is not available')
            input('Press enter...')
