import datetime

DATE_FORMAT = '%Y-%m-%d'


def handle_error(message):
    """
    Display an error message and prompt the user to press enter.
    :param message: The error message to display.
    """
    print(message)
    input('Press enter...')


def validate(date_text):
    """
    Validate the date format.
    :param date_text: A string representing a date in the format YYYY-MM-DD.
    """
    try:
        datetime.datetime.strptime(date_text, DATE_FORMAT)
    except ValueError:
        handle_error("Incorrect data format, should be YYYY-MM-DD")


def validate_int(data):
    """
    Validate if the given data can be converted to an integer.
    :param data: The data to be validated.
    :return: The converted integer value if successful, False otherwise.
    """
    try:
        return int(data)
    except ValueError:
        handle_error('Wrong data type')
        return False