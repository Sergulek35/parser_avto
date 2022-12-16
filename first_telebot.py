import telebot
from os import getenv
from dotenv import load_dotenv
from func_parser import parce_car

# TommyBot -   Имя бота
# TOKEN = 5811397292:AAHbu1pHdrZWeYDrqK36ogXoIo5TvSWRh08

load_dotenv()

TOKEN = getenv('token')
bot = telebot.TeleBot(TOKEN)

info = []


@bot.message_handler(commands=['start'])
def examination(message):
    hey = message.from_user.first_name
    bot.reply_to(message, f'Добро пожаловать, {hey}')
    bot.reply_to(message, '👋')


@bot.message_handler(commands=['help'])
def examination(message):
    # print(message)
    bot.reply_to(message, 'команды:\nstart - Приветствие\n'
                          'help - Помощь\n'
                          'parc - Парсинг новых авто, от "AVANTA"\n'
                          'file - Данные команды "parc" в файле\n'
                          'Если вводим сообщение - то заменяются буквы а и о\n'
                          '🤝')


@bot.message_handler(commands=['file'])
def get_file(message):
    parce_car()
    chat_id = message.chat.id
    with open('car_brands.txt') as f:
        bot.send_document(chat_id, f)


@bot.message_handler(commands=['parc'])
def info_a(message):
    # print(message)
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{parce_car()}')


@bot.message_handler(content_types=['text'])
def send_sticker(message):
    # print(message)
    text = message.text.upper()
    for i in text:
        if i == "О":
            i = '😂'
        elif i == 'А':
            i = '🅰'
        info.append(i)
    bot.reply_to(message, f'{info}')
    info.clear()


bot.polling()
