# -*- coding: utf-8 -*-
import requests
import os
import time
import pycurl
import logging
from urllib.parse import urlencode
from pymongo import MongoClient

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')
PSID = os.getenv('PSID', '')
URI_TELEGRAM = os.getenv('URI_TELEGRAM', '')
URI_FACEBOOK = os.getenv('URI_FACEBOOK', '')

print(TELEGRAM_ACCESS_TOKEN)
print(FACEBOOK_ACCESS_TOKEN)
print(PSID)
print(URI_TELEGRAM)
print(URI_FACEBOOK)


def get_telegram_users(message):
    client = MongoClient(URI_TELEGRAM)
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


def get_facebook_users(message):
    client = MongoClient(URI_FACEBOOK)
    db = client['lino_facebook']

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
    day = time.strftime('%A', time.localtime())

    if day in build_valid_days():
        # Change the url if you have your own webcrawler server
        try:
            response = requests.get(
                'http://webcrawler-ru.lappis.rocks/cardapio/{}/Desjejum'
                .format(day)
            ).json()
        except ValueError:
            logging.warning('Decoding JSON has failed')
            response = None
    else:
        response = None

    return response


def build_valid_days():
    return [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]


def parse_daily_notification_to_json(menu):
    messages = []
    messages.append('E no café da manhã de hoje teremos: ')

    text = ''
    for item in menu:
        prev = item
        item = item.replace(':', '')
        text += '*{}*'.format(item) + ':' + ' ' + menu[prev] + '\n'

    messages.append(text)

    return messages


def notify_daily_meal_to_telegram(messages, telegram_users):
    chats = telegram_users

    for chat in chats:
        for message in messages:

            requests.get(
                'https://api.telegram.org/bot{}\
                /sendChatAction?chat_id={}&action=typing'
                .format(TELEGRAM_ACCESS_TOKEN, chat['sender_id'])).json()

            time.sleep(1)

            requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}\
                &parse_mode=Markdown'
                .format(TELEGRAM_ACCESS_TOKEN, chat['sender_id'], message)
            ).json()


def notify_daily_meal_to_facebook(messages, facebook_users):
    chats = facebook_users

    for chat in chats:
        for message in messages:
            builded_message = build_facebook_message(
                chat['sender_id'],
                message + '\n'
            )

            postfields = urlencode(builded_message)

            url = get_url_facebook_parameter()

            curl = pycurl.Curl()
            curl.setopt(curl.URL, url)
            curl.setopt(curl.POSTFIELDS, postfields)
            curl.perform()
            curl.close()


def build_facebook_message(sender_id, message):
    return {
        'recipient': {
            'id': sender_id
        },
        'message': {
            'text': message
        }
    }


def get_url_facebook_parameter():
    return ('https://graph.facebook.com/v2.6/{}/messages?access_token={}'
            .format(PSID, FACEBOOK_ACCESS_TOKEN))


menu = get_daily_menu()

telegram_users = get_telegram_users('breakfast meal')
facebook_users = get_facebook_users('breakfast meal')

if menu:
    messages = parse_daily_notification_to_json(menu)
    notify_daily_meal_to_telegram(messages, telegram_users)
    notify_daily_meal_to_facebook(messages, facebook_users)
else:
    messages = []
    messages.append('Não consegui pegar o café da manhã pra você hoje... :(')
    messages.append('Parece que teve algum problema com o site do RU')
    notify_daily_meal_to_telegram(messages, telegram_users)
    notify_daily_meal_to_facebook(messages, facebook_users)
