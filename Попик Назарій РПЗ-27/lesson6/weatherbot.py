#pip3 install pytelegrambotapi
import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

conf = get_default_config()
conf['language'] = 'en'

token = '5400961963:AAF4vO0GSBoRGj5gemsG68EA7XYRA6prN3U'
key = '7c465062a0f180b7ad20fc0d38a3c66b'

owm = OWM(key, conf)
manager = owm.weather_manager()

#API - application program interface

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def greetings(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('Action 1', 'Action 2') #for more info search register_next_step_handler
    bot.send_message(message.chat.id, 'Hello!',reply_markup=markup)
    print(message.chat.id)

@bot.message_handler(commands=['chatId'])
def getChatId(message):
    bot.send_message(message.chat.id, message.chat.id)
    print(message.chat.id)

@bot.message_handler(content_types=['text'])
def getWeather(message):
    try:
        weather = manager.weather_at_place(message.text).weather
        temperature = weather.temperature("celsius")["temp"]
        pressure = weather.pressure["press"]
        sunrise_date = weather.sunrise_time(timeformat='date')
        sunset_date = weather.sunset_time(timeformat='date')
        
        response = str(temperature) + '\n' + str(pressure) + '\n' + str(sunrise_date) + '\n' + str(sunset_date)
        
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, f'Could not find "{message.text}"')
    
bot.polling(non_stop = True)