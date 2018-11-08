import requests
import os
import time
import logging
import pycurl
import logging
from rasa_core.actions.action import Action
from urllib.parse import urlencode

TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')

class ActionDailyDinner(Action):
    def name(self):
        return "action_daily_dinner"

    def run(self, dispatcher, tracker, domain):
        messages = []

        day = time.strftime('%A', time.localtime())

        tracker_state = tracker.current_state()
        logging.warning(tracker_state)
        sender_id = tracker_state['sender_id']

        try:
            response = requests.get(
                'http://webcrawler-ru.lappis.rocks/cardapio/{}'
                .format(day)
            ).json()
        except KeyError as keyexception:
            logging.info(keyexception)
            dispatcher.utter_message("É final de semana, amigo... Não tem RU não kkkk")

        if(day is not 'Saturday' and day is not 'Sunday'):
            
            lunch_menu = ""

            for label in response['JANTAR']:
                dish = str('*' + label + '*' + ' ' + response['JANTAR'][label] + '\n')
                lunch_menu += dish

            messages.append(lunch_menu)

            welcome_message = 'Eai! Então... Pro jantar, nós teremos: '

            data = requests.get(
                'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
                .format(TELEGRAM_ACCESS_TOKEN, sender_id,welcome_message)
            ).json()
            messenger = ""
            # Check user is from Telegram or Facebook
            if not data['ok']:
                dispatcher.utter_message(welcome_message)
                messenger = "Facebook"
            else:
                messenger = "Telegram"

            if(messenger == "Telegram"):
                for message in messages:
                    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=Markdown'
                    .format(TELEGRAM_ACCESS_TOKEN,sender_id, message))
            elif(messenger == "Facebook"):
                for message in messages:
                    dispatcher.utter_message(message)

        return []

    # def run(self, dispatcher, tracker, domain):
    #     messages = []

    #     day = time.strftime('%A', time.localtime())

    #     # Change the url if you have your own webcrawler server
    #     try:
    #         response = requests.get(
    #             'http://webcrawler-ru.lappis.rocks/cardapio/{}'
    #             .format(day)
    #         ).json()
    #     except KeyError as keyexception:
    #         logging.info(keyexception)
    #         messages.append("É final de semana, amigo... Não tem RU não kkkk")

    #     messages.append('Eai! Então... Pro jantar, nós teremos: ')

    #     dinner_menu = ""

    #     for label in response['JANTAR']:
    #         dish = str(label + ': ' + response['JANTAR'][label] + '\n')
    #         dinner_menu += dish

    #     messages.append(dinner_menu)

    #     for message in messages:
    #         dispatcher.utter_message(message)

    #     return []