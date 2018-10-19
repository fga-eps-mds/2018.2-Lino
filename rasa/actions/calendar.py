import requests
import time
import os
import yaml
from pprint import pprint
from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

# If you have your own database, changes to ('database', <PORT>)
client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
db = client.lino_ru

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('ACCESS_TOKEN', '625051845:AAGFkfemDjiriY4uRdIR7ayujxLdzwileLg')

class ActionCalendar(Action):
    def name(self):
        return "utter_calendar"

    def run(self, dispatcher, tracker, domain):
        messages = []
        messages.append('DEU BOM')
        for m in messages: dispatcher.utter_message(m)
        return []
