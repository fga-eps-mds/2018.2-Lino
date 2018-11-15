import os
import requests
import json
from pymongo import MongoClient
from rasa_core.actions.action import Action

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

TELEGRAM_DB_URI = os.getenv('TELEGRAM_DB_URI', '')
FACEBOOK_DB_URI = os.getenv('FACEBOOK_DB_URI', '')


class ActionUnregisterNotification(Action):
    def name(self):
        return "action_unregister_notification"

    def run(self, dispatcher, tracker, domain):
        messages = []

        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']

        text = tracker_state['latest_message']['text']

        text = text.lower()
        words_list = text.split(' ')
        words_key_list = self.build_key_words()

        notification = ""

        for word in words_list:
            if word in words_key_list:
                notification = self.get_element_in_notification_map(word)
                break

        if notification is "":
            dispatcher.utter_message(('Não consegui encontrar essa opção... '
                                      'Dá uma olhada melhor nas opções, '
                                      'só temos elas, ainda!'))
            return []

        user_checked = False

        user_telegram = self.check_telegram_valid_user(sender_id)
        user_facebook = self.check_facebook_valid_user(sender_id)
        welcome = ('Agora você já não recebe mais esse tipo de notificação... '
                   'Quer receber ou retirar outra?')
        if user_telegram != {}:
            user_checked = self.check_user_not_receive_notification(
                sender_id, TELEGRAM_DB_URI, 'lino_telegram', notification)

            if user_checked:
                self.update_telegram_user(user_telegram, notification)
                messages.append(welcome)

        elif user_facebook != {}:
            user_checked = self.check_user_not_receive_notification(
                sender_id, FACEBOOK_DB_URI, 'lino_facebook', notification)

            if user_checked:
                self.update_facebook_user(user_facebook, notification)
                messages.append(welcome)

        if user_checked:
            for message in messages:
                data = self.remove_markup_telegram(message, sender_id)
                if not data['ok']:
                    dispatcher.utter_message(message)
        else:
            message = ('Essa notificação já está desativada! Você quer '
                       'escolher outra opção?')
            data = self.remove_markup_telegram(message, sender_id)
            if not data['ok']:
                dispatcher.utter_message(message)

        return []

    def check_user_not_receive_notification(
            self, sender_id, URI, database, notification):

        client = MongoClient(URI)
        db = client[database]

        user_notifications = db.users.find_one(
            {'sender_id': sender_id},
            {'_id': 0, 'notification': 1}
        )

        notifications = user_notifications['notification']

        notification_stats = False

        for element in notifications:
            if element['description'] in notification and element['value']:
                notification_stats = True
                break

        return notification_stats

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
        URI = TELEGRAM_DB_URI
        database = 'lino_telegram'

        self.update_notification(
            notification,
            URI,
            database,
            user_telegram
        )

        return []

    def update_facebook_user(self, user_facebook, notification):
        URI = FACEBOOK_DB_URI
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
                element['value'] = False
                break

        db.users.update(
            {'sender_id': user['sender_id']},
            {'$set': {'notification': notification_list}}
        )

        return []

    def check_telegram_valid_user(self, sender_id):
        client = MongoClient(TELEGRAM_DB_URI)
        db_telegram = client['lino_telegram']

        user = {}
        user = db_telegram.users.find_one({'sender_id': sender_id})

        if user is None:
            return {}
        else:
            return user

    def check_facebook_valid_user(self, sender_id):
        client = MongoClient(FACEBOOK_DB_URI)
        db_facebook = client['lino_facebook']

        user = {}
        user = db_facebook.users.find_one({'sender_id': sender_id})

        if user is None:
            return {}
        else:
            return user

    def remove_markup_telegram(self, message, sender_id):
        """
        Sends a message using Telegram API and removes any KeyboardMarkup.
        Returns a dict with the API response.
        """
        reply_markup = {
            "remove_keyboard": True
        }

        remove_keyboard_payload = {
            "chat_id": sender_id,
            "text": "just a text",
            "reply_markup": json.dumps(reply_markup)
        }

        remove_keyboard_payload['text'] = message
        data = requests.post(
            ('https://api.telegram.org/bot{}'
             '/sendMessage')
            .format(TELEGRAM_ACCESS_TOKEN),
            data=remove_keyboard_payload
        ).json()
        return data
