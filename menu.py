import sys
from enum import Enum

from functions import chosen_currency_status
from validators import validate_int
from functions import clearconsole, get_currencies_table, ask_value, bid_value


class ChoiceEnum(Enum):
    LIST_AVAILABLE_CURRENCIES = 1
    SEL_OR_BUY = 2
    CHOOSE_CURRENCY = 3
    LOG_OUT = 4


def list_currencies():
    get_currencies_table()


def sell_or_buy():
    option = input('Please write "SELL" or "BUY": ')
    if option.upper() == 'SELL':
        currency = input("Please write currency short name: ")
        amount = int(input("Please write amount: "))
        ask_value(currency, amount)
    elif option.upper() == 'BUY':
        currency = input("Please write currency short name: ")
        amount = int(input("Please write amount: "))
        bid_value(currency, amount)
    else:
        print('Wrong typing, try again')
        input('Press enter...')


def choose_currency():
    currency = input('Enter the currency you want to check: ')
    rate_number = 1
    print(chosen_currency_status(currency, rate_number))
    input('Press enter...')


def log_out():
    print('End.')
    sys.exit(0)


def run_calculation(choice):
    functions[choice]()


functions = {
    ChoiceEnum.LIST_AVAILABLE_CURRENCIES.value: list_currencies,
    ChoiceEnum.SEL_OR_BUY.value: sell_or_buy,
    ChoiceEnum.CHOOSE_CURRENCY.value: choose_currency,
    ChoiceEnum.LOG_OUT.value: log_out,

}


def print_options():
    print('1. Print available currencies: ')
    print('2. Do You want sell or buy currency?: ')
    print('3. Please choose currency: ')
    print('4. Exit: ')


def validate_decision(decision):
    allowed_decisions = [e.value for e in ChoiceEnum]
    if decision not in allowed_decisions:
        clearconsole()
        print(f"Number {decision} is  not permitted!")
        input('Press enter...')
        run()
    else:
        return False


def check_user_input(data):
    if data.isdigit():
        return False
    else:
        print('Wrong user input.')


def run():
    while True:
        clearconsole()
        print_options()
        decision = input('Please select option: ')
        if decision == "":
            print('You do not press any key....')
            input('Press enter...')
        if decision != "":
            try_int = validate_int(decision)
            if try_int:
                validate_decision(try_int)
                clearconsole()
                run_calculation(try_int)
