import requests
import time
import os
import yaml
from pprint import pprint
from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

CREDENTIALS = os.getenv('CREDENTIALS', '../credentials.yml')

class ActionHello(Action):
    def name(self):
        return "custom_greet"
    
    def run(self, dispatcher, tracker, domain):
        messages = []
        a = tracker.current_state()
        print(a)
        messages.append('Hello baby!')
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
        text = 'Olá'
        configs = yaml.load(open(CREDENTIALS))
        token = configs['access_token']
        data = requests.get(
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}').json()
        print('SAVING IN THE DATABASE')
        pprint(data)
        new_user = {}
        new_user['sender_id'] = id
        new_user['name'] = data['result']['chat']['first_name'] + ' ' + data['result']['chat']['last_name']
        client = MongoClient(f'mongodb://test:test2018@ds239930.mlab.com:39930/lino_ru')
        db = client.lino_ru
        db.users.insert_one(new_user)
        pprint(new_user)
        print('SAVED IN DATABASE')
        return []