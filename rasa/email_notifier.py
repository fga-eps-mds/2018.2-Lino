# -*- coding: utf-8 -*-
import requests
import os
import time
import os
from pymongo import MongoClient
from pprint import pprint
from notification_config import db_user, db_password, telegram_token

client = MongoClient('mongodb://http://ds041831.mlab.com:41831/newAlert')
db = client.239258843822-cgk0toiq0bjuga3213t1qm0vhgh5gjh2.apps.googleusercontent.com
telegram_token = os.getenv('ACCESS_TOKEN', '')

telegram_token = os.getenv('ACCESS_TOKEN', '')


def getUsers():
    notifications = db.notifications
    result = notifications.find_one()
    print(result)
    return result['users_list']
    
def getEmail():
    day = time.strftime('%A',time.localtime())
    response = requests.get('http://localhost:3000/newAlert').json()
    return response

def parseJson(res):
    messages = []
    messages.append('Vou ver se tem um e-mail pra você aqui: ')
    for item in res:
        if item.status == 200:
            text = 'Você tem um novo e-mail!' + '\n'
        elif item.status == 404:
            text = 'Parece que ninguém te mandou nada. Try again later' + '\n'
        else:
            text = 'Amigo, não to te achando aqui na lista de e-mail' + '\n'
        messages.append(text)
        return messages

def notify(messages):
    chats = getUsers()
    for item in messages:
        item = item.replace(' ', '+')
    for id in chats:
        for text in messages:
            a = requests.get(
                'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'.format(telegram_token, id)).json()
            time.sleep(1)
            a = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(telegram_token, id, text)).json()

res = getEmail()
res = parseJson(res)
a = notify(res)
