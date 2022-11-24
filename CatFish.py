 import telebot
 import os
 import random as r
 import time
 #Мои библиотеки----------
 from Kurs_Rub import kurs
 from data import clock
  
 #Вывод сообщения о том что бот запущен
 f = open('zap.txt','r')
 print(*f)
 
 #Привязываем свою программу к телеграмм-боту вместь "Your Tocen" вставляем его токен
 bot = telebot.TeleBot('Your Tocen')
  
 @bot.message_handler(commands=['help','secret','kurs'])
 
 def comands(message):
     if message.text == '/help':
         bot.send_message(message.chat.id, '/secret - секрет \n /kurs - курс рубля')
  
     if message.text == '/secret':
         bot.send_message(message.chat.id, 'Секрет успешно активирован')
         img = 'https://yandex.ru/images/search?text=%20%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5&from=tabbar&pos='+str(r.randint(1,1000))+'&img_url=https%3A%2F%2Fget.wallhere.com%2Fphoto%2Fillustration-blonde-long-hair-anime-anime-girls-lookin
         bot.send_photo(message.chat.id, photo=img)
  
     if message.text == '/kurs':
         bot.send_message(message.chat.id, 'команда /kurs включена.')
         if clock.time() == '18:30':
            k = 'Сила российского рубля на '+ clock.data(1) +' составляет: \n' + kurs.RUB()
            bot.send_message(message.chat.id, k)
bot.polling()
