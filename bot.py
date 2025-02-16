import telebot
import requests

TOKEN = "7856028217:AAFvPgpUdunaStrSSVI9Q3eETBgm4z4GFBs"
bot = telebot.TeleBot(TOKEN)

def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    return response.json()["price"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to CryptoSignals AI! 🚀\nGet free crypto trading signals daily.")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    btc_price = get_crypto_price()
    bot.reply_to(message, f"Today's Signal: BUY BTC at ${btc_price} 🚀")

bot.polling()
import time

while True:
    def send_signal():
    signal = get_btc_price()
    bot.send_message(chat_id, signal)
import requests

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    price = response.json()['price']
    return f"BUY BTC at ${price}"
