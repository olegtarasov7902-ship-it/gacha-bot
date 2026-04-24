import telebot
from flask import Flask
from threading import Thread

BOT_TOKEN = '8708415476:AAFiu-sUnwvf031Izn8grrrrruBOtHLN7Jc'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Привет! Я echo-бот. Всё работает!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"Ты сказал: {message.text}")

# Keep alive (обязательно для Render)
app = Flask('')
@app.route('/')
def home():
    return "Бот жив"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
print("Запускаю echo-бота...")
bot.remove_webhook()
bot.polling(none_stop=True)
