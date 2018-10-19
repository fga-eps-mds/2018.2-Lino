import requests
import time
import os
import logging
from pprint import pprint
from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

# If you have your own database, changes to ('database', <PORT>)
client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
db = client.lino_ru

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

class ActionStart(Action):
    def name(self):
        return "custom_start"

    def run(self, dispatcher, tracker, domain):
        # Create a list message to chat with user
        messages = []

        # Tracker that stores the state of dialogue, to gets the users id
        tracker = tracker.current_state()
        sender_id = tracker['sender_id']

        # Creates an attribute to specify the host messenger
        messenger = "None"

        # Message to send to the user
        text = "Adoro conhecer pessoas novas! Calma aí rapidinho, vou anotar seu nome na minha agenda..."

        # Get users data to build a user to the database
        data = requests.get(
            f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={sender_id}&text={text}').json()

        # Check if user data was get succefully
        if data['ok'] == False:
            data = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,last_name&access_token={}".format(sender_id, PAGE_ACCESS_TOKEN)).json()
            client = MongoClient('mongodb://mongo_facebook:27011/lino_facebook')
            db = client['lino_facebook']

            messenger = "Facebook"
        else:
            client = MongoClient('mongodb://mongo_telegram:27010/lino_telegram')
            db = client['lino_telegram']

            messenger = "Telegram"

        # Get all users that are registered and check if
        users_data = list(db.users.find({}, {'sender_id': 1, '_id': 0}))

        users_id = []
        for users in users_data:
            users_id.append(users['sender_id'])

        if sender_id in users_id:
            # User found in the database
            messages.append('Eai! Já tenho você aqui na minha agenda, ' + \
                            'ajeitei algumas coisas pra você...')
            messages.append('Agora eu posso te enviar alguns avisos, principalmente ' + \
                            'se for relacionado ao RU ou avisos da comunidade acadêmica.')
            for message in messages:
                dispatcher.utter_message(message)
            return []
        else:
            # New user to be registered
            if messenger == "Facebook":
                messages.append(text)

                for message in messages:
                    dispatcher.utter_message(message)

        # Difference user between avaiable messengers
        if messenger is "Telegram":
            new_data = self.build_telegram_user(data, sender_id)
            self.save_telegram_user(new_data, db)
        elif messenger is "Facebook":
            new_data = self.build_facebook_user(data, sender_id)
            self.save_facebook_user(new_data, db)

        return []

    def build_telegram_user(self, data, sender_id):
        first_name = ""
        last_name = ""

        first_name = data['result']['chat']['first_name']

        try:
            last_name = data['result']['chat']['last_name']
        except AttributeError as exception:
            print("Telegram user has not a last name!")

        notification_list = self.build_notification_list()

        return {
            'sender_id': sender_id,
            'name': first_name + ' ' + last_name,
            'notification': notification_list
        }

    def build_facebook_user(self, data, sender_id):
        print(data)

        first_name = ""
        last_name = ""

        first_name = data['first_name']

        try:
            last_name = data['last_name']
        except AttributeError as exception:
            print("Facebook user has not a last name!")

        notification_list = self.build_notification_list()

        return {
            'sender_id': sender_id,
            'name': first_name + ' ' + last_name,
            'notification': notification_list
        }

    def build_notification_list(self):
        # Build notification_list structure
        return [
            {'description': 'daily meal', 'value': False},
            {'description': 'week meal', 'value': False},
            {'description': 'breakfast meal', 'value': False},
            {'description': 'lunch meal', 'value': False},
            {'description': 'dinner meal', 'value': False},
            {'description': 'gmail alert', 'value': False},
        ]

    def save_telegram_user(self, user_data, db_telegram):
        # Build user structure and save in telegram database
        db_telegram.users.insert_one(user_data)
        logging.info('User save in telegram database')
        return []

    def save_facebook_user(self, user_data, db_facebook):
        # Build user structure and save in facebook database
        db_facebook.users.insert_one(user_data)
        logging.info('User save in facebook database')
        return []

class ActionAskNotification(Action):
    def name(self):
        return "action_ask_notification"

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
