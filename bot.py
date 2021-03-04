import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN, PROXY

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    username = update['message']['chat']['username']
    update.message.reply_text(f'Привет {username}! Ты вызвал команду /start!')


def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    mybot = Updater(TOKEN, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
