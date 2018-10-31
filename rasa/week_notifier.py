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

    try:
        response = requests.get(
            'https://webcrawler-ru.lappis.rocks/cardapio/pdf'
        ).json()
    except ValueError:
        logging.warning('Decoding JSON has failed')
        response = None

    return response
