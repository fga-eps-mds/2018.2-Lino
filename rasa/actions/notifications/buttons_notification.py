import os
from rasa_core.actions.action import Action

# If you want to use your own bot to development add the bot token as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')

TELEGRAM_DB_URI = os.getenv('TELEGRAM_DB_URI', '')
FACEBOOK_DB_URI = os.getenv('FACEBOOK_DB_URI', '')


class ActionButtonsNotification(Action):
    def name(self):
        return "action_buttons_notification"

    def run(self, dispatcher, tracker, domain):
        buttons_facebook = None
        buttons_telegram = None

        try:
            message = 'Qual das opções você deseja?'
            buttons_telegram = self.build_buttons_telegram()
            dispatcher.utter_button_message(message,
                                            buttons_telegram,
                                            button_type="custom")
        except ValueError as valueException:
            print(valueException + ': on Telegram')

        if not buttons_telegram:
            try:
                buttons_facebook = self.build_buttons_facebook()
                elements = self.build_facebook_elements(buttons_facebook)
                dispatcher.utter_custom_message(*elements)
            except ValueError as valueException:
                print(valueException + ': on Messenger')

        return []

    def build_button_dict(self):
        return [
            ('Alerta da Comunidade',
             'alerta da comunidade'),
            ('Cardápio do Dia', 'dia'),
            ('Cardápio da Semana', 'semana'),
            ('Café da Manhã', 'café'),
            ('Almoço', 'almoço'),
            ('Jantar', 'jantar')
        ]

    def build_facebook_message(self, sender_id, message, buttons):
        return {
            'recipient': {
                'id': sender_id
            },
            'message': {
                'text': message,
                'attachment': {
                    'type': 'template',
                    'payload': {
                        'template_type': 'generic',
                        'elements': self.build_facebook_elements(buttons)
                    }
                }
            }
        }

    def build_facebook_elements(self, buttons):
        message = 'Qual das opções você deseja?'
        elements = []
        for value in buttons:
            element = self.build_element(value, message)
            elements.append(element)
        return elements

    def build_element(self, list_buttons, message):
        return {
            'title': message,
            'buttons': list_buttons
        }

    def build_buttons_facebook(self):
        values = self.build_button_dict()
        lista = [values[x:x+3]for x in range(0, len(values), 3)]
        print(lista)
        for value in lista:
            for i in range(0, len(value)):
                value[i] = {
                    'type': 'postback',
                    'title': value[i][0],
                    'payload': value[i][1]
                }
        return lista

    def build_buttons_telegram(self):
        values = self.build_button_dict()
        lista = [values[x:x+3]for x in range(0, len(values), 3)]
        for value in lista:
            for i in range(0, len(value)):
                value[i] = {
                    'title': value[i][0],
                    'payload': value[i][1]
                }
        return lista
