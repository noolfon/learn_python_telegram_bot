import logging

from handlers import greet_user, guess_number, send_cat_picture, user_coordinates, talk_to_me
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(TOKEN, use_context=True, )  # request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
