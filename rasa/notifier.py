import requests
import time
from pymongo import MongoClient
from pprint import pprint
from notification_config import db_user, db_password, telegram_token

client = MongoClient(f'mongodb://{db_user}:{db_password}@ds239930.mlab.com:39930/lino_ru')
db = client.lino_ru

def getUsers():
    notifications = db.notifications
    result = notifications.find_one()
    print(result)
    return result['users_list']

def getMenu():
    day = time.strftime('%A',time.localtime())
    response = requests.get(f'http://localhost:5000/cardapio/{day}').json()
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
                f'https://api.telegram.org/bot{telegram_token}/sendChatAction?chat_id={id}&action=typing').json()
            pprint(a)
            time.sleep(2)
            a = requests.get(
                f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={id}&text={text}').json()
            pprint(a)

res = getMenu()
res = parseJson(res)
a = notify(res)