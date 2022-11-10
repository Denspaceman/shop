import os
from datetime import datetime
import random
import re
import json

import telebot

# Read constant from environment variables available to edit at my.selectel.ru
TOKEN = os.environ.get('TOKEN')

HELP_MSG = """
Commands usage help:
/start to start
/sticker to get a sticker :-) It's so simple for now!
/getwebhook <token of your telegram bot>
/setwebhook <token of your telegram bot> <url to call on message>
"""

# Create `bot` instance to use some features from pyTelegramBotAPI package.
# WARN: Not all of them is useful in serverless architecture.
bot = telebot.TeleBot(token=TOKEN, threaded=False)
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('/sticker', '/start')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

def main(**kwargs):
    """
    Serverless environment entry point.
    """
    bot.infinity_polling()
