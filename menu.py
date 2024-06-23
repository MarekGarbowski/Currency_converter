import sys
from enum import Enum
from functions import chosen_currency_status
from validators import validate_int
from functions import clearconsole, get_currencies_table, ask_value, bid_value


class ChoiceEnum(Enum):
    """
    This module contains the `ChoiceEnum` class which is an enumeration representing different choices available in a program. The enumeration values are:

    - `LIST_AVAILABLE_CURRENCIES`: Represents the choice to list available currencies.
    - `SEL_OR_BUY`: Represents the choice to select or buy a currency.
    - `CHOOSE_CURRENCY`: Represents the choice to choose a specific currency.
    - `LOG_OUT`: Represents the choice to log out of the program.

    Example Usage:
    -------------
    from enum import Enum

    class ChoiceEnum(Enum):
        LIST_AVAILABLE_CURRENCIES = 1
        SEL_OR_BUY = 2
        CHOOSE_CURRENCY = 3
        LOG_OUT = 4

    # Access the enumeration values
    print(ChoiceEnum.LIST_AVAILABLE_CURRENCIES)  # Output: ChoiceEnum.LIST_AVAILABLE_CURRENCIES

    # Compare two enumeration values
    print(ChoiceEnum.LIST_AVAILABLE_CURRENCIES == ChoiceEnum.SEL_OR_BUY)  # Output: False

    # Iterate over the enumeration values
    for choice in ChoiceEnum:
        print(choice)  # Output: ChoiceEnum.LIST_AVAILABLE_CURRENCIES, ChoiceEnum.SEL_OR_BUY, ChoiceEnum.CHOOSE_CURRENCY, ChoiceEnum.LOG_OUT
    """
    LIST_AVAILABLE_CURRENCIES = 1
    SEL_OR_BUY = 2
    CHOOSE_CURRENCY = 3
    LOG_OUT = 4


def list_currencies():
    """

    """
    get_currencies_table()


def sell_or_buy():
    """
    This function prompts the user to choose between "SELL" or "BUY" and then accepts input for currency and amount.
    If the user inputs a valid option ('SELL' or 'BUY'), the function calls either the ask_value() or the bid_value() function, passing in the currency and amount as arguments.
    If the user inputs an invalid option, the function displays an error message and prompts the user to try again.
    After each prompt, the function waits for the user to press the enter key.

    :return: None
    """
    option = input('Please write "SELL" or "BUY": ').upper()
    if option == 'SELL' or option == 'BUY':
        currency = input("Please write currency short name: ")
        try:
            amount = int(input("Please write amount: "))
        except ValueError:
            print("Amount must be an integer.")
            input('Press enter...')
            return
        if option == 'SELL':
            ask_value(currency, amount)
        else:
            bid_value(currency, amount)
    else:
        print('Wrong typing, try again')
        input('Press enter...')


def choose_currency():
    """
    Choose Currency

    This function prompts the user to input a currency and a rate number, and then calls another function `chosen_currency_status` to retrieve and display the status of the chosen currency.

    :return: None
    """
    currency = input('Enter the currency you want to check: ')
    try:
        rate_number = int(input('Enter rate number: '))
    except ValueError:
        print("Rate number must be an integer.")
        input('Press enter...')
        return
    print(chosen_currency_status(currency, rate_number))
    input('Press enter...')


def log_out():
    """
    Logs out the user and terminates the program.

    :return: None
    """
    sys.exit(0)


def run_calculation(choice):
    """
    Run a calculation based on the user's choice.

    :param choice: The user's choice to determine which calculation to run.
    :type choice: str
    :return: None
    """
    action = functions.get(int(choice))
    if action:
        action()
    else:
        print(f"Invalid choice: {choice}")


functions = {
    ChoiceEnum.LIST_AVAILABLE_CURRENCIES.value: list_currencies,
    ChoiceEnum.SEL_OR_BUY.value: sell_or_buy,
    ChoiceEnum.CHOOSE_CURRENCY.value: choose_currency,
    ChoiceEnum.LOG_OUT.value: log_out,
}


def print_options():
    """
    Prints out the available options for the user to choose from.

    :return: None

    Example usage:
        >>> print_options()
        1. Print available currencies:
        2. Do You want sell or buy currency?:
        3. Please choose currency:
        4. Exit:
    """
    print('1. Print available currencies: ')
    print('2. Do You want sell or buy currency?: ')
    print('3. Please choose currency: ')
    print('4. Exit: ')


def validate_decision(decision):
    """
    Validate the decision.

    :param decision: The decision to validate.
    :return: True if the decision is valid; otherwise, it clears the console, displays an error message, waits for user input, and restarts the program.
    """
    allowed_decisions = [e.value for e in ChoiceEnum]
    if decision not in allowed_decisions:
        clearconsole()
        print(f"Number {decision} is not permitted!")
        input('Press enter...')
        run()
    else:
        return True


def check_user_input(data):
    """
    Checks if the input data is a digit.

    :param data: The input data to be checked.
    :return: True if the input data is a digit, False otherwise.
    """
    if data.isdigit():
        return True
    else:
        print('Wrong user input.')
        return False


def run():
    """
    The `run()` function is the main function of the program. It repeatedly clears the console, displays available options, takes user input, and performs the corresponding action based on the input.

    :return: None
    """
    while True:
        clearconsole()
        print_options()
        decision = input('Please select option: ')
        if not decision:
            print('You did not press any key....')
            input('Press enter...')
        elif check_user_input(decision):
            try_int = validate_int(decision)
            if validate_decision(try_int):
                clearconsole()
                run_calculation(try_int)
