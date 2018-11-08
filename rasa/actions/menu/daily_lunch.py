import requests
import time
from rasa_core.actions.action import Action
import logging

class ActionDailyLunch(Action):
    def name(self):
        return "action_daily_lunch"

    def run(self, dispatcher, tracker, domain):
        messages = []

        day = time.strftime('%A', time.localtime())

        # Change the url if you have your own webcrawler server
        try:
            response = requests.get(
                'http://webcrawler-ru.lappis.rocks/cardapio/{}'
                .format(day)
            ).json()
        except KeyError as keyexception:
            logging.info(keyexception)
            messages.append("É final de semana, amigo... Não tem RU não kkkk")

        messages.append('Tava na hora hein. Pro almoço teremos: ')

        lunch_menu = ""

        for label in response['ALMOÇO']:
            dish = str(label + ': ' + response['ALMOÇO'][label] + '\n')
            lunch_menu += dish

        messages.append(lunch_menu)

        for message in messages:
            dispatcher.utter_message(message)

        return []