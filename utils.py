from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import randint, choice
from emoji import emojize

from config import USER_EMOJI

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_numbers(user_number):
    rand_number = randint(user_number - 10, user_number + 10)
    if user_number > rand_number:
        message = f'Вы ввели число {user_number}, оно больше {rand_number}. Поздравляю вы выиграли!'
    elif user_number == rand_number:
        message = f'Вы ввели число {user_number}, оно больше {rand_number}. Ничья!'
    else:
        message = f'Вы ввели число {user_number}, оно меньше {rand_number}. Вы проиграли!'
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['/cat', 'Прислать котика', KeyboardButton('Мои координаты', request_location=True)],
                                ['/start', '/guess']], resize_keyboard=True)