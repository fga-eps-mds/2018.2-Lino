# -*- coding: utf-8 -*-
import requests
import os
import time
from pymongo import MongoClient

telegram_token = os.getenv('ACCESS_TOKEN', '')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

URL = os.getenv('WEBHOOK_URL', '')


def getTelegramUsers():
    client = MongoClient('mongodb://mongo-telegram:27010/lino_telegram')
    db = client['lino_telegram']

    users = db.users.find({"notification": {"description": "gmail alert",
                           "value": True}}, {'_id': 0, 'sender_id': 1})
    return users


def getFacebookUsers():
    client = MongoClient('mongodb://mongo-facebook:27011/lino_facebook')
    db = client['lino_facebook']

    users = db.users.find({"notification": {"description": "gmail alert",
                           "value": True}}, {'_id': 0, 'sender_id': 1})
    return users


def getEmail():
    response = requests.get(URL).json()
    return response


def parseJson(response):
    message = ""
    if response == "Forbidden":
        message = ""
    elif response == "No new messages found":
        message = ""
    else:
        message = 'Vocẽ recebeu e-mail. Dá uma olhada aí' + '\n' + '\n' + \
                str(response['email']) + '\n' + 'Assunto: ' + \
                str(response['subject']) + '\n' + 'Mensagem: ' + \
                str(response['message'])
    return message


def notifyTelegram(message):
    chats = getTelegramUsers()
    if chats is None:
        return

    for id in chats:
        requests.get(
            'https://api.telegram.org/bot{}/sendChatAction?chat_id='
            .format(telegram_token, id) +
            '{}&action=typing'.format(id)
        )

        time.sleep(1)

        requests.get(
            'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
            .format(telegram_token, id, str(message))).json()


def notifyFacebook(message):
    chats = getFacebookUsers()
    if chats is None:
        return

    for user in chats:
        requests.get(
            'https://graph.facebook.com/v2.6/{}/messages?access_token={}'
            .format(user['sender_id'], PAGE_ACCESS_TOKEN)
        )


result = getEmail()
response = parseJson(result)
notifyTelegram(str(response))
notifyFacebook(str(response))
