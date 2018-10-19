# -*- coding: utf-8 -*-
import requests
import os
import time
import os
from pymongo import MongoClient
from pprint import pprint
from notification_config import db_user, db_password

# If you have your own database, changes to ('database', <PORT>)
client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
db = client.lino_ru

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('ACCESS_TOKEN', '625051845:AAGFkfemDjiriY4uRdIR7ayujxLdzwileLg')


def getUsers():
    notifications = db.notifications
    result = notifications.find_one()

    print(result)

    return result['users_list']

def getMenu():
    day = time.strftime('%A',time.localtime())

    # Change the url if you have your own webcrawler server
    response = requests.get('http://webcrawler-ru.lappis.rocks/cardapio/{}'.format(day)).json()

    return response


def parseJson(res):
    messages = []
    messages.append('E hoje no RU nós teremos: ')

    for item in res:
        if item != 'DESJEJUM':
            text = 'Para o ' + item.lower() + ':\n'
        else:
            text = 'Para o ' + 'café da manhã:' + '\n'

        for sub in res[item]:
            text += sub + ' ' + res[item][sub] + '\n'

        messages.append(text)

    return messages


def notify(messages):
    chats = getUsers()

    for item in messages:
        item = item.replace(' ', '+')

    for id in chats:
        for text in messages:
            a = requests.get(
                'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'
                .format(telegram_token, id)).json()

            time.sleep(1)
            a = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
                .format(telegram_token, id, text)).json()

res = getMenu()
res = parseJson(res)
a = notify(res)
