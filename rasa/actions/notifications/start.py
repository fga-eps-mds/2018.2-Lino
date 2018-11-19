import requests
import os
import logging
from pymongo import MongoClient
from rasa_core.actions.action import Action

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

TELEGRAM_DB_URI = os.getenv('TELEGRAM_DB_URI', '')
FACEBOOK_DB_URI = os.getenv('FACEBOOK_DB_URI', '')


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
        text = ('Pera aí, rapidinho... '
                'Vou pegar minha agenda aqui pra te procurar')

        # Get users data to build a user to the database
        data = requests.get(
            'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
            .format(TELEGRAM_ACCESS_TOKEN, sender_id, text)
        ).json()

        # Check if user data was get succefully
        if not data['ok']:
            data = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,"
                .format(sender_id) +
                "last_name&access_token={}"
                .format(FACEBOOK_ACCESS_TOKEN)
            ).json()

            client = MongoClient(FACEBOOK_DB_URI)
            db = client['lino_facebook']

            messenger = "Facebook"
        else:
            client = MongoClient(TELEGRAM_DB_URI)
            db = client['lino_telegram']

            messenger = "Telegram"

        # Get all users that are registered and check if
        users_data = list(db.users.find({}, {'sender_id': 1, '_id': 0}))

        users_id = []
        for users in users_data:
            users_id.append(users['sender_id'])

        print(users_id)

        if sender_id in users_id:
            # User found in the database
            for message in messages:
                dispatcher.utter_message(message)
            return []
        else:
            text = ('Olha! Acho que não tenho você aqui hein! Calma aí '
                    'rapidinho, vou anotar seu nome na minha agenda...')

            # New user to be registered
            if messenger == "Facebook":

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
        except KeyError as exception:
            print("Telegram user has not a last name!")
            logging.info(exception)

        notification_list = self.build_notification_list()

        return {
            'sender_id': sender_id,
            'name': first_name + ' ' + last_name,
            'notification': notification_list
        }

    def build_facebook_user(self, data, sender_id):
        first_name = ""
        last_name = ""

        first_name = data['first_name']

        try:
            last_name = data['last_name']
        except KeyError as exception:
            print("Facebook user has not a last name!")
            logging.info(exception)

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
