import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(
message,
"স্বাগতম VIP1 Membership বটে।"
)

print("Bot running...")
bot.infinity_polling()
