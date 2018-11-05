# -*- coding: utf-8 -*-
import requests
import os
import time
import pycurl
from pymongo import MongoClient
from urllib.parse import urlencode


telegram_token = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')
PSID = os.getenv('PSID', '')
URI_TELEGRAM = os.getenv('URI_TELEGRAM', '')
URI_FACEBOOK = os.getenv('URI_FACEBOOK', '')


def get_telegram_users():
    client = MongoClient(URI_TELEGRAM)
    db = client['lino_telegram']

    users = db.users.find({"notification": {"description": "gmail alert",
                           "value": True}}, {'_id': 0, 'sender_id': 1})
    return users


def get_facebook_users():
    client = MongoClient(URI_FACEBOOK)
    db = client['lino_facebook']

    users = db.users.find({"notification": {"description": "gmail alert",
                           "value": True}}, {'_id': 0, 'sender_id': 1})
    return users


def get_email():

    URL = "https://lino-alerta.lappis.rocks/newAlert"

    try:
        response = requests.get(URL).json()
    except ValueError as valueException:
        print(valueException)
        response = None

    return response


def parse_json(response):
    message = ""
    if response == "Forbidden":
        message = ""
    elif response == "No new messages found":
        message = ""
    else:
        message = 'Tem um novo e-mail rolando... Dá uma olhada aí' + \
                '\n' + '\n' + \
                str(response['email']) + '\n' + 'Assunto: ' + \
                str(response['subject']) + '\n' + 'Mensagem: ' + \
                str(response['message'])
    return message


def notify_telegram(message, telegram_users):
    chats = telegram_users
    if chats is None:
        return

    for chat in chats:
        requests.get(
            'https://api.telegram.org/bot{}/sendChatAction?chat_id={}'
            .format(telegram_token, chat['sender_id']) +
            '&action=typing'
        )

        time.sleep(1)

        requests.get(
            'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
            .format(telegram_token, chat['sender_id'], message)).json()


def notify_facebook(message, facebook_users):
    chats = facebook_users
    if chats is None:
        return

    for chat in chats:
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
            .format(PSID, PAGE_ACCESS_TOKEN))


result = get_email()

telegram_users = get_telegram_users()
facebook_users = get_facebook_users()

if result:
    response = parse_json(result)
    if response != "":
        notify_telegram(response, telegram_users)
        notify_facebook(response, facebook_users)
