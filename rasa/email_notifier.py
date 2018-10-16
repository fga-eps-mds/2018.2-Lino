# -*- coding: utf-8 -*-
import requests
import urllib, json
import os
import time
import os
from pprint import pprint

telegram_token = os.getenv('ACCESS_TOKEN', '659699316:AAHdYVzLxQnSJZMyGpfC5FnegYR16GNQzUA')

URL = 'http://localhost:5003/newAlert'

def getEmail():
    response = requests.get(URL).json()
    return response

def parseJson(response):
    message = ""
    if response == "Forbidden":
        message = 'Jovem, não to te achando aqui na lista de e-mail' + '\n'
    elif response == "No new messages found":
        message = 'Parece que ninguém te mandou nada. Try again later' + '\n'
    else:
        message = response
    return message

def notify(message):
    chats = []
    for id in chats:
        #    a = requests.get(
         #       'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'.format(telegram_token, id)).json()
          #  time.sleep(1)
            a = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(telegram_token, id, str(message))).json()

result = getEmail()
response = parseJson(result)
notify(response)