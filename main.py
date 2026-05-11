import telebot

# استبدل 'رمز_البوت_الخاص_بك' برمز البوت الفعلي الخاص بك
TOKEN = '8410949251:AAHW8GkHA724nfIh0v-64niN-VJKcWK1ZzM'
bot = telebot.TeleBot(TOKEN)

# معالج الأوامر لأمر '/start'
@bot.message_handler(commands=['start'])
def ارسال_الترحيب(message):
    bot.reply_to(message, "مرحباً بك في البوت!\nاستخدم /help لمشاهدة الأوامر المتاحة.")

# معالج الأوامر لأمر '/help'
@bot.message_handler(commands=['help'])
def ارسال_المساعدة(message):
    bot.send_message(
    message.chat.id,
    "مرحباً بك في البوت!\nاستخدم /help لمشاهدة الأوامر المتاحة."
    )

# هنا يمكنك إضافة المزيد من الأوامر والميزات

# بدء التصويت
if __name__ == '__main__':
    bot.polling()
