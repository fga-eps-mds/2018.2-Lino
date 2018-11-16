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


class ActionListNotifications(Action):
    """
    Lists all the notification types the user is registered in.
    """
    def name(self):
        return "action_list_notifications"

    def run(self, dispatcher, tracker, domain):
        messages = []
        messages.append('Você está cadastrado nesses tipos de notificação:')
        state = tracker.current_state()
        sender_id = state['sender_id']

        telegram, facebook = self.db_connect()

        user = telegram.find_one({'sender_id': sender_id})

        if not user:
            user = facebook.find_one({'sender_id': sender_id})

        notifications = list(self.registered_types(user))

        types = ''
        for notification in notifications:
            name = self.get_notification_type(notification['description'])
            types += '* ' + name + '\n'
        messages.append(types)

        messages.append('Quer realizar alguma outra operação?')

        for message in messages:
            data = self.remove_markup_telegram(message, sender_id)
            if not data['ok']:
                dispatcher.utter_message(message)

        return []

    def registered_types(self, user):
        for item in user['notification']:
            if item['value']:
                yield item

    def db_connect(self):
        telegram_client = MongoClient(TELEGRAM_DB_URI)
        facebook_client = MongoClient(FACEBOOK_DB_URI)

        telegram_db = telegram_client['lino_telegram']
        facebook_db = facebook_client['lino_facebook']

        telegram = telegram_db['users']
        facebook = facebook_db['users']

        return (telegram, facebook)

    def get_notification_type(self, word):
        notification_map = {
            'daily meal': 'Cardápio do Dia',
            'week meal': 'Cardápio da Semana',
            'breakfast meal': 'Café da Manhã',
            'lunch meal': 'Almoço',
            'dinner meal': 'Jantar',
            'gmail alert': 'Alertas da Comunidade'
        }

        try:
            result = notification_map[word]
            return result
        except KeyError as err:
            print(err)
            return None

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
