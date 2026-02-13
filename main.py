import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '8551896844:AAGB3J3CM_Qy0_ylAF3EaO7JTbjRdJChv_k'
bot = telebot.TeleBot(TOKEN)

# Command handler for the '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot!\nUse /help to see available commands.")

# Command handler for the '/help' command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
    message.chat.id,
    "Welcome to the bot!\nUse /help to see available commands."
    )

# This is where you can add more commands and features

# Start polling
if __name__ == '__main__':
    bot.polling()
