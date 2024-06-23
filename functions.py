import requests
import os
import json


def get_currency_rates(currency, rate_number, table):
    """
    Function to get currency rates from the NBP API.
    :param currency: The currency code to retrieve rates for.
    :param rate_number: The number of rates to retrieve.
    :param table: The table name from which to retrieve rates.
    :return: The raw data retrieved from the API.
    """
    try:
        url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/last/{rate_number}/?format=json'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Return JSON directly
    except requests.HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')


def chosen_currency_status(currency, rate_number):
    """
    This function returns the status of a chosen currency.
    :param currency: The currency to check the status for.
    :param rate_number: The rate number to use for checking the currency status.
    :return: The status of the chosen currency.
    """
    data = get_currency_rates(currency, rate_number, "c")
    if data:  # Check if data is None
        currency_name = str(data.get('currency', 'UNKNOWN')).upper()
        rates = data.get('rates', [])
        if rates:
            currency_ask = rates[0].get('ask', 0)
            currency_bid = rates[0].get('bid', 0)
            result = f'The currency: {currency_name} in:\n' \
                     f'sale is for: {currency_ask} PLN,\n' \
                     f'purchase for: {currency_bid} PLN'
            return result
    return "Currency data could not be retrieved"


def get_currencies_table():
    """
    This function retrieves currency exchange rates from the NBP API and prints them to the console.
    :return: None
    """
    try:
        url = "http://api.nbp.pl/api/exchangerates/tables/a/today/?format=json"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data_json = response.json()
    except requests.HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        for word in data_json:
            counter = 0
            for keys in word.values():
                counter += 1
                if counter == 4:
                    for currency in keys:
                        print(f'Currency: {currency["currency"]}, '
                              f'code {currency["code"]}, mid price is: {currency["mid"]} PLN')


def ask_value(currency, amount):
    """
    Ask for a value in a specific currency.
    :param currency: The currency code (e.g., USD, EUR) to convert to.
    :param amount: The amount to convert.
    :return: None
    """
    data = get_currency_rates(currency, 1, "c")
    if data:
        currency_ask = amount * data['rates'][0].get('ask', 0)
        print(currency_ask)


def bid_value(currency, amount):
    """
    Function to calculate the bid value for a given currency and amount.
    :param currency: A string representing the currency code.
    :param amount: A float representing the amount of currency to be bid.
    :return: None
    """
    data = get_currency_rates(currency, 1, "c")
    if data:
        currency_bid = amount * data['rates'][0].get('bid', 0)
        print(currency_bid)


def clearconsole():
    """
    Clears the console screen.
    :return: None
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
