import telebot 
# Importē bibliotēku darbam ar Telegram botiem
import json
import requests  

# Izveido Telegram bota objektu (šeit jāievieto bota token no BotFather)

API = 'ece18f14b0d7c351b1f78f51761a8957'
# OpenWeatherMap API atslēga, kas ļauj pieprasīt laikapstākļu datus


@bot.message_handler(commands=['start'])
# Norāda, ka zemāk esošā funkcija tiks izpildīta, kad lietotājs ieraksta /start komandu
def start(message):
    bot.send_message(message.chat.id,'Hello! I glad to see you! write the name of the city')
    # Nosūta lietotājam sveicienu un aicina ierakstīt pilsētas nosaukumu


@bot.message_handler(content_types=['text'])
# Norāda, ka zemāk esošā funkcija apstrādās visas teksta ziņas
def get_weather(message):
    city = message.text.strip().lower()
    # Paņem lietotāja ziņu, noņem atstarpes un pārveido uz mazajiem burtiem

    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric') # type: ignore
    # Izveido HTTP GET pieprasījumu uz OpenWeatherMap ar lietotāja pilsētu un tavu API atslēgu

    if res.status_code == 200:
        # Ja pieprasījums bija veiksmīgs (statuss 200), tad turpina

        data = json.loads(res.text)
        # Pārvērš JSON tekstu par Python vārdnīcu 

        temp = data["main"]["temp"]
        # No iegūtajiem datiem paņem temperatūru

        bot.reply_to(message, f'current weather:{temp} ')
        # Nosūta lietotājam ziņu ar pašreizējo temperatūru

        image = 'sun.jpg' if temp > 5.0 else 'sunny.png'
        # Ja temperatūra ir virs 5°C, izvēlas attēlu "sunny.png", citādi – "sun.png"

        file = open('./' + image,'rb')
        # Atver izvēlēto attēla failu lasīšanai binārajā režīmā

        bot.send_photo(message.chat.id, file)
        # Nosūta attēlu kā foto lietotājam

    else:
        # Ja statusa kods nav 200, laikapstākļus neizdevās atrast

        bot.reply_to(message, f'Sorry, I could not find the weather. Please try again later.')
        # Paziņo lietotājam, ka laikapstākļus neizdevās atrast

bot.polling(none_stop=True)
# Sāk bota nepārtrauktu ziņu pārbaudi (polling režīmā), lai tas vienmēr klausītos lietotāju ziņās
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('7765096350:AAG_ZsLVnF-sbvKqrhn4I7-MXkRLyIHm6ic'))
API = os.getenv('ece18f14b0d7c351b1f78f51761a8957')
