from emoji import emojize
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN, PROXY, USER_EMOJI

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.message.chat.username
    update.message.reply_text(f'Привет {username}{context.user_data["emoji"]}! Ты вызвал команду /start!')


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f'{text}, {context.user_data["emoji"]}')


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


def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Играем: введите число'
    return update.message.reply_text(message)


def send_cat_picture(update, context):
    cat_photos_list = glob('img/cat*.jp*g')
    cat_photo_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))


def main():
    mybot = Updater(TOKEN, use_context=True, )  # request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
