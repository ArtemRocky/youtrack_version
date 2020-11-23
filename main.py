#!/usr/bin/python
import requests
import telebot
from bs4 import BeautifulSoup
from multiprocessing import Process
import time



bot = telebot.TeleBot(token='YOUR_BOT_TOKEN')
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('check')

#parce check actual youtrack version
url = 'https://www.jetbrains.com/shop/download/YTDN50/2020500'
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)
with open("test.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("tbody"):
        print("{0}: {1}".format(tag.name, tag.text))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, tag.text, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'check':
        bot.send_message(message.from_user.id, tag.text, reply_markup=keyboard)

#sending messages by timer
def check_send_messages():
    while True:
        bot.send_message(#YOUR_TG_ID, tag.text, reply_markup=keyboard)
        time.sleep(60)
p1 = Process(target=check_send_messages, args=())
p1.start()


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)


