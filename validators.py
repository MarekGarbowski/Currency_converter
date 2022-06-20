import datetime


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        input('Press enter...')


# def sell_or_buy_option(data):
#     if data == 'SELL':
#         return True
#     else:
#         return False


def validate_int(data):
    try:
        x = int(data)
    except ValueError:
        print('Wrong data type')
        input('Press enter...')
        return False
    else:
        return x
