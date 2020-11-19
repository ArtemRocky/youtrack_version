#!/usr/bin/python
import requests
import telebot
import config
from bs4 import BeautifulSoup
from multiprocessing import Process
import time
#import logging
#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)

#parce check actual youtrack version
url = 'https://www.jetbrains.com/shop/download/YTDN50/2020400'
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)
with open("test.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("tbody"):
        print("{0}: {1}".format(tag.name, tag.text))

bot = telebot.TeleBot(config.token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('check')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(419216849, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'check':
        bot.send_message(419216849, tag.text, reply_markup=keyboard)


#sending messages by timer
def check_send_messages():
    while True:
        bot.send_message(419216849, tag.text, reply_markup=keyboard)
        time.sleep(3600)
p1 = Process(target=check_send_messages, args=())
p1.start()


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
