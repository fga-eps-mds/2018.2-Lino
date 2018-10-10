# -*- coding: utf-8 -*-
import requests
import os
import time
import os
from pymongo import MongoClient
from pprint import pprint
from notification_config import db_user, db_password, telegram_token

telegram_token = os.getenv('ACCESS_TOKEN', '')

def getEmail():
    response = requests.get('http://localhost:3000/newAlert').json()
    return response

def parseJson(res):
    messages = []
    for item in res:
        if item.status == 200:
            text = 'Você tem um novo e-mail!' + '\n'
            messages.append(text)
        elif item.status == 404:
            text = 'Parece que ninguém te mandou nada. Try again later' + '\n'
        else:
            text = 'Amigo, não to te achando aqui na lista de e-mail' + '\n'
        messages.append(text)
        return messages
        for text in messages:

def notify(messages):
    chats = getUsers()
    for item in messages:
        item = item.replace(' ', '+')
    for id in chats:
            a = requests.get(
                'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'.format(telegram_token, id)).json()
            time.sleep(1)
            a = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(telegram_token, id, text)).json()

res = getEmail()
res = parseJson(res)
a = notify(res)
