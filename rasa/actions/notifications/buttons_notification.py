import os
from pymongo import MongoClient
from rasa_core.actions.action import Action

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

TELEGRAM_DB_URI = os.getenv('TELEGRAM_DB_URI', 'localhost')
FACEBOOK_DB_URI = os.getenv('FACEBOOK_DB_URI', 'localhost')

class ActionButtonsNotification(Action):
    def name(self):
        return "action_buttons_notification"

    def run(self, dispatcher, tracker, domain):
        buttons = self.build_button_telegram()
        mensagem = 'VAI TOMAR NO CU'
        dispatcher.utter_button_message(mensagem, buttons, button_type="custom")
        return []

    def build_button_dict(self):
        return [
            ('cardápio diario','dia'),
            ('cardápio semanal', 'semana'),
            ('alerta da comunidade', 'comunidade'),
            ('café da manhã', 'café'),
            ('jantar', 'jantar'),
            ('almoço', 'almoço')
        ]
        
    
    def build_button_facebook(self):
        pass
    
    def build_button_telegram(self):
        values = self.build_button_dict()
        lista = [values[x:x+3]for x in range(0, len(values), 3)]
        for value in lista: 
            for i in range(0, len(value)):
                value[i] = {
                    'title': value[i][0],
                    'payload': value[i][1]
                }
        return lista




        


    
