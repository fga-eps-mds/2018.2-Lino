import os
from pymongo import MongoClient
from rasa_core.actions.action import Action

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')


class ActionCalendar(Action):
    def name(self):
        return "action_calendar"

    def run(self, dispatcher, tracker, domain):
        messages = []
        messages.append(
            'Em breve você terá acesso aos dados sobre o período de MATRÍCULA!'
        )
        for m in messages:
            dispatcher.utter_message(m)
        return []
