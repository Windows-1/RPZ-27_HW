import telebot

token = '5400961963:AAF4vO0GSBoRGj5gemsG68EA7XYRA6prN3U'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, 'How old are you?',)
    

@bot.message_handler(content_types=['text'])
def old_check(message):
    try:
        age = int(message.text)
        if age >=100:
            bot.send_message(message.chat.id, f'Are you sure? "{message.text}"')
        elif age >= 18:
            bot.send_message(message.chat.id, 'You are adult')
        elif age >=0:
            bot.send_message(message.chat.id, 'You are child')
        else:
            bot.send_message(message.chat.id, f'Are you sure? "{message.text}"')
    except:
        bot.send_message(message.chat.id, 'Error! Type only numbers')


bot.polling(non_stop=True)