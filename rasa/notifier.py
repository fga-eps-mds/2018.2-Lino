# -*- coding: utf-8 -*-
import requests
import os
import time
from pymongo import MongoClient

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('ACCESS_TOKEN', '')

def get_telegram_users(message):
    client = MongoClient('mongodb://mongo_telegram:27010/lino_telegram')
    db = client['lino_telegram']

    users = db.users.find(
        {
            "notification": {
                "description": message,
                "value": True
            }
        },
        {
            '_id': 0,
            'sender_id': 1
        }
    )

    return users

def get_daily_menu():
    day = time.strftime('%A',time.localtime())

    if day in build_valid_days():
        # Change the url if you have your own webcrawler server
        response = requests.get('http://webcrawler-ru.lappis.rocks/cardapio/{}'.format(day)).json()
    else:
        response = None

    return response

def build_valid_days():
    return [
        'Monday',
        'Tuesday'
        'Wednesday',
        'Thursday',
        'Friday'
    ]

def parse_daily_notification_to_json(menu):
    messages = []
    messages.append('E no cardápio de hoje, no RU, nós teremos: ')

    for item in menu:
        if item != 'DESJEJUM':
            text = 'Para o ' + item.lower() + ':\n'
        else:
            text = 'Para o ' + 'café da manhã:' + '\n'

        for sub_item in menu[item]:
            text += sub_item + ' ' + menu[item][sub_item] + '\n'

        messages.append(text)

    return messages


def notify_daily_meal(messages):
    chats = get_telegram_users('daily meal')

    for chat in chats:
        for message in messages:

            requests.get(
                'https://api.telegram.org/bot{}/sendChatAction?chat_id={}&action=typing'
                .format(telegram_token, chat['sender_id'])).json()

            time.sleep(1)

            requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
                .format(telegram_token, chat['sender_id'], message)).json()


menu = get_daily_menu()

if menu:
    messages = parse_daily_notification_to_json(menu)
    notify_daily_meal(messages)
