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
telegram_token = os.getenv('ACCESS_TOKEN', '')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN', '')
PSID = os.getenv('PSID', '')


def get_facebook_users(message):
    client = MongoClient('mongodb://mongo_facebook:27011/lino_facebook')
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

    response = {
        'status': 'ok',
        'url': "https://ru.unb.br/images/Cardapio/outubrorefeitorio2018/" +
        "FUPFGAFCE29-10-a-04-11.pdf"
    }

    # try:
    #     response = requests.get(
    #         'https://webcrawler-ru.lappis.rocks/cardapio/pdf'
    #     ).json()
    # except ValueError:
    #     logging.warning('Decoding JSON has failed')
    #     response = None

    return response


def notify_daily_meal_to_facebook(message):
    chats = get_facebook_users('week meal')

    for chat in chats:
        builded_message = build_facebook_message(
            chat['sender_id'], message['url']
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
                "type": "file",
                "payload": {
                    "url": url
                }
            }
        }
    }


def get_url_facebook_parameter():
    return ('https://graph.facebook.com/v2.6/{}/messages?access_token={}'
            .format(PSID, PAGE_ACCESS_TOKEN))


message = get_weekly_menu()

if message:
    notify_daily_meal_to_telegram(message)
    notify_daily_meal_to_facebook(message)
