# -*- coding: utf-8 -*-
import requests
import os
import pycurl
import time
from urllib.parse import urlencode
from pymongo import MongoClient

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')
PSID = os.getenv('PSID', '')
URI_TELEGRAM = os.getenv('URI_TELEGRAM', '')
URI_FACEBOOK = os.getenv('URI_FACEBOOK', '')


def get_telegram_users(message):
    client = MongoClient(URI_TELEGRAM)
    db = client['lino_telegram']

    users = db.users.find(
        build_query(message),
        build_filters()
    )

    return users


def get_facebook_users(message):
    client = MongoClient(URI_FACEBOOK)
    db = client['lino_facebook']

    users = db.users.find(
        build_query(message),
        build_filters()
    )

    return users


def build_query(message):
    return {
        'notification': {
            'description': message,
            "value": True
        }
    }


def build_filters():
    return {
        '_id': 0,
        'sender_id': 1
    }


def get_weekly_menu():

    response = 'https://webcrawler.guilhesme.rocks/cardapio/pdf'

    return response


def notify_daily_meal_to_telegram(message, telegram_users):
    chats = telegram_users

    comment_message = "Tá aqui o cardápio da semana"

    for chat in chats:
        requests.get(
            'https://api.telegram.org/bot{}\
            /sendChatAction?chat_id={}&action=typing'
            .format(TELEGRAM_ACCESS_TOKEN, chat['sender_id'])).json()

        time.sleep(1)

        requests.get(
            'https://api.telegram.org/bot{}/sendPhoto?'
            .format(TELEGRAM_ACCESS_TOKEN) +
            'chat_id={}&photo={}&caption={}'
            .format(chat['sender_id'],
                    message,
                    comment_message)
            ).json()


def notify_daily_meal_to_facebook(message, facebook_users):
    chats = facebook_users

    for chat in chats:
        builded_message = build_facebook_message(
            chat['sender_id'], message
        )

        postfields = urlencode(builded_message)

        url = get_url_facebook_parameter()

        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.POSTFIELDS, postfields)
        curl.perform()
        curl.close()


def build_facebook_message(sender_id, url):
    return {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url
                }
            }
        }
    }


def get_url_facebook_parameter():
    return ('https://graph.facebook.com/v2.6/{}/messages?access_token={}'
            .format(PSID, FACEBOOK_ACCESS_TOKEN))


message = get_weekly_menu()

telegram_users = get_telegram_users('weekly meal')
facebook_users = get_facebook_users('weekly meal')

if message:
    notify_daily_meal_to_telegram(message, telegram_users)
    notify_daily_meal_to_facebook(message, facebook_users)
