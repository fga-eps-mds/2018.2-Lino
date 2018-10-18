# -*- coding: utf-8 -*-
import requests
import os
import time

telegram_token = os.getenv('ACCESS_TOKEN', '')

URL = os.getenv('WEBHOOK_URK', '')


def getEmail():
    response = requests.get(URL).json()
    return response


def parseJson(response):
    message = ""
    if response == "Forbidden":
        message = 'Jovem, não to te achando aqui na lista de e-mail' + '\n'
    elif response == "No new messages found":
        message = ""
    else:
        message = 'Vocẽ recebeu e-mail. Dá uma olhada aí' + '\n' + '\n' + \
                'Remetente: ' + str(response['email']) + '\n' + 'Assunto: ' + \
                str(response['subject']) + '\n' + 'Mensagem: ' + \
                str(response['message'])
    return message


def notify(message):
    chats = []
    for id in chats:
        requests.get(
            'https://api.telegram.org/bot{}/sendChatAction?chat_id='
            .format(telegram_token, id) +
            '{}&action=typing'.format(id)).json()

        time.sleep(1)

        requests.get(
            'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
            .format(telegram_token, id, str(message))).json()


result = getEmail()
response = parseJson(result)
notify(str(response))
