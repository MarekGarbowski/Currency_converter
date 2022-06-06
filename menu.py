import sys
from enum import Enum


class ChoiceEnum(Enum):
    LIST_AVAILABLE_CURRENCIES = 1
    SEL_OR_BUY = 2
    CHOOSE_CURRENCY = 3
    SELL = 4
    BUY = 5
    LOG_OUT = 6


def list_currencies():
    pass


def sell_or_buy():
    pass


def choose_currency():
    pass


def sell():
    pass


def buy():
    pass


def log_out():
    print('End.')
    sys.exit(0)


def run_calculation(choice):
    functions[choice]()


functions = {
    ChoiceEnum.LIST_AVAILABLE_CURRENCIES.value: list_currencies,
    ChoiceEnum.SEL_OR_BUY.value: sell_or_buy,
    ChoiceEnum.CHOOSE_CURRENCY.value: choose_currency,
    ChoiceEnum.SELL.value: sell,
    ChoiceEnum.BUY.value: buy,
    ChoiceEnum.LOG_OUT.value: log_out,

}


def print_options():
    print('1. Print available currencies: ')
    print('2. Do You want SELL or BUY currency?: ')
    print('3. Please choose currency: ')
    print('4. Write amount to sell: ')
    print('5. Write amount to buy: ')
    print('6. Exit: ')


def validate_decision(decision):
    allowed_decisions = [e.value for e in ChoiceEnum]
    if decision not in allowed_decisions:
        raise Exception(f"Number {decision} is  not permitted!")


while True:
    print_options()
    decision = int(input('Please select option: '))
    validate_decision(decision)
    run_calculation(decision)
