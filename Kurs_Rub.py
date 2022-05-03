import requests
from bs4 import BeautifulSoup
import pandas as pd

class kurs:
    def __init__():
        pass

    def RUB():

        #берем информацию  с сайта
        URL = "https://www.cbr.ru/currency_base/daily/"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'lxml')
        quotes = soup.find_all('table', class_='data')
        for quote in quotes:
            RUB = quote.text

        EURO = int(RUB[484:486])
        USD = int(RUB[459:461])

        #Берем информацию с прошлого курса
        file = open('Kurs.txt','r')
        content = file.read()
        b_USD = int(content[0:2])
        b_EURO = int(content[3:5])

        #Запись текщего курса
        file = open('Kurs.txt','w+')
        file.write(str(USD)+' '+str(EURO))
        file.close()

        a_USD = str(USD - b_USD)
        a_EURO =str(EURO - b_EURO)

        KURS = '$ = ' + str(USD) + '₽\n' + '€ = ' + str(EURO) + '₽\n' + 'Укрепление по сравнеинию с предыдущим днем:\n' + '$ = ' + a_USD + '₽\n' + '€ = ' + a_EURO + '₽'
        return KURS
