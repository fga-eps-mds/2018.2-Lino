import requests
from pymongo import MongoClient
from notification_config import db_user, db_password, telegram_token

client = MongoClient(f'mongodb://{db_user}:{db_password}@ds239930.mlab.com:39930/lino_ru')
db = client.lino_ru

def getUsers():
    notifications = db.notifications
    result = notifications.find_one()
    print(result)
    return result['users_list']

def notify(text):
    chats = getUsers()
    text = text.replace(' ','+')
    for id in chats:
        requests.get(f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={id}&text={text}').json()

a = notify('Notification')