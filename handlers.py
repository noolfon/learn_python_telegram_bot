from glob import glob
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.message.chat.username
    update.message.reply_text(
        f'Привет {username}{context.user_data["emoji"]}! Ты вызвал команду /start!', reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f'{text}, {context.user_data["emoji"]}')


def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Играем: введите число'
    return update.message.reply_text(message, reply_markup=main_keyboard())


def send_cat_picture(update, context):
    cat_photos_list = glob('img/cat*.jp*g')
    cat_photo_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup=main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.message.chat.username
    coord = update.message.location
    update.message.reply_text(
        f'{username}{context.user_data["emoji"]}! Твои координаты {coord}', reply_markup=main_keyboard())