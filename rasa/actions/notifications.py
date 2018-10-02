import requests
import time
import os
import yaml
from pprint import pprint
from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
db = client.lino_ru

class ActionHello(Action):
    def name(self):
        return "custom_greet"

    def run(self, dispatcher, tracker, domain):
        messages = []
        a = tracker.current_state()
        print(a)
        messages.append('Yeaaaah!')
        messages.append('Seu id é: ' + str(a['sender_id']))
        for message in messages:
            dispatcher.utter_message(message)
        return []

class ActionStart(Action):
    def name(self):
        return "custom_start"

    def run(self, dispatcher, tracker, domain):
        messages = []
        a = tracker.current_state()
        id = a['sender_id']
        token = os.getenv('ACCESS_TOKEN', '')
        data = requests.get(
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}').json()
        print('SAVING IN THE DATABASE')
        new_user = {}
        id_user = {}
        id_user['sender_id'] = id
        new_user['sender_id'] = id
        new_user['name'] = data['result']['chat']['first_name'] + ' ' + data['result']['chat']['last_name']
        users = db.users.find({}, {'sender_id': 1, '_id': 0})
        users = list(users)
        if id_user not in users:
            db.users.insert_one(new_user)
            print('SAVED IN DATABASE')
        else:
            print('ALREADY EXISTS')
        return []

class ActionAskNotification(Action):
    def name(self):
        return "action_ask_notification"

    def run(self, dispatcher, tracker, domain):
        messages = []
        a = tracker.current_state()
        id = a['sender_id']
        print('SAVING IN THE DATABASE')
        notifications = db.notifications.find_one()
        user_list = []
        if not notifications:
            new_users = []
            new_users.append(id)
            db.notifications.insert_one({
                'id': 1,
                'description': 'menu_day',
                'users_list': new_users
            })
            messages.append('A partir de agora vc receberá notificações do RU')
        else:
            user_list = notifications['users_list']
        if id not in user_list:
            user_list.append(id)
            db.notifications.update_one({'id': 1}, {
                '$set': {'users_list': user_list}
            })
            messages.append('A partir de agora vc receberá notificações do RU!')
            print('SAVED IN DATABASE')
        else:
            messages.append('Você já está na lista de usuários cadastrados!')
            print('ALREADY EXISTS')
        dispatcher.utter_message('Okay!')
        for m in messages: dispatcher.utter_message(m)
        return []
