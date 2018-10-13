# -*- coding: utf-8 -*-
import requests
import urllib, json
import os
import time
import os
from pprint import pprint

telegram_token = os.getenv('ACCESS_TOKEN', '')

URL = 'http://localhost:3000/newAlert'

def getEmail():
    response = requests.get(url = URL)
    data = response.json()
    return response

def parseJson(res):
    messages = []
    for response in res:
        if response.get == 200:
            text = url.date + '\n' + url.name + '\n' + url.email + '\n' + url.subject + '\n' + url.message
            messages.append(text)
        elif response.get == 404:
            text = 'Parece que ninguém te mandou nada. Try again later' + '\n'
        else:
            text = 'Jovem, não to te achando aqui na lista de e-mail' + '\n'
        messages.append(text)
        return messages

def notify(messages):
    chats = getEmail()
    for response in messages:
        response = response.replace(' ', '+')
    for id in chats:
            a = requests.get(
                'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'.format(telegram_token, id)).json()
            time.sleep(1)
            a = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(telegram_token, id, text)).json()

res = getEmail()
res = parseJson(res)
a = notify(res)
