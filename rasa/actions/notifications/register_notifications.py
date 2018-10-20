import requests
import time
import os
import logging
from pprint import pprint
from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')


class ActionRegisterNotification(Action):
    def name(self):
        return "action_register_notification"

    def run(self, dispatcher, tracker, domain):
        messages = []

        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']

        text = tracker_state['latest_message']['text']

        words_list = text.split(' ')
        words_key_list = self.build_key_words()

        notification = ""

        for word in words_list:
            if word in words_key_list:
                notification = self.get_element_in_notification_map(word)
                break

        user_telegram = self.check_telegram_valid_user(sender_id)
        user_facebook = self.check_facebook_valid_user(sender_id)

        if user_telegram != {}:
            self.update_telegram_user(user_telegram, notification)
        else:
            self.update_facebook_user(user_facebook, notification)

        messages.append('Agora você pode receber notificações desse tipo...')

        for message in messages:
            dispatcher.utter_message(message)

        return []

    def build_key_words(self):
        return [
            'café',
            'almoço',
            'jantar',
            'dia',
            'semana',
            'comunidade'
        ]

    def get_element_in_notification_map(self, word):
        notification_map = {
            'dia': 'daily meal',
            'semana': 'week meal',
            'café': 'breakfast meal',
            'almoço': 'lunch meal',
            'jantar': 'dinner meal',
            'comunidade': 'gmail alert'
        }

        return notification_map[word]


    def update_telegram_user(self, user_telegram, notification):
        URI = 'mongodb://mongo_telegram:27010/lino_telegram'
        database = 'lino_telegram'

        self.update_notification(
            notification,
            URI,
            database,
            user_telegram
        )

        return []

    def update_facebook_user(self, user_facebook, notification):
        URI = 'mongodb://mongo_facebook:27011/lino_facebook'
        database = 'lino_facebook'

        self.update_notification(
            notification,
            URI,
            database,
            user_facebook
        )

        return []

    def update_notification(self, notification, URI, database, user):
        client = MongoClient(URI)
        db = client[database]

        notification_list = user['notification']

        for element in notification_list:
            if element['description'] == notification:
                element['value'] = True
                break

        db.users.update({'sender_id': user['sender_id']},
            {'$set': {'notification': notification_list}}
        )

        return []

    def check_telegram_valid_user(self, sender_id):
        client = MongoClient('mongodb://mongo_telegram:27010/lino_telegram')
        db_telegram = client['lino_telegram']

        user = {}
        user = db_telegram.users.find_one({'sender_id': sender_id})

        if user == None:
            return {}
        else:
            return user

    def check_facebook_valid_user(self, sender_id):
        client = MongoClient('mongodb://mongo_facebook:27011/lino_facebook')
        db_facebook = client['lino_facebook']

        user = {}
        user = db_facebook.users.find_one({'sender_id': sender_id})

        if user == None:
            return {}
        else:
            return user