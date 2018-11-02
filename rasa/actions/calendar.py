import os
from pymongo import MongoClient
from rasa_core.actions.action import Action

# If you have your own database, changes to ('database', <PORT>)
client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
db = client.lino_ru

# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('ACCESS_TOKEN', '')


class ActionCalendar(Action):
    def name(self):
        return "action_calendar"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Ja to indo...')
        crawlerRegister = 'https://webcrawler-matricula.lappis.rocks'
        data = {}
        data = {
            'text': 'Calendário de matrícula',
            'image': f'{crawlerRegister}/registration/downloadPdf'
            }
        dispatcher.utter_response(data)
        return []
