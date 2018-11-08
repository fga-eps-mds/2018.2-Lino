import requests
import os
import time
import pycurl
import logging
from urllib.parse import urlencode

TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '688895966:AAHF8fFDZxVjtyHjn-PkAlEQ93IhV52MWbg')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN','')

class ActionDailyBreakfast(Action):
    def name(self):
        return "action_daily_breakfast"

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
            messages.append("É final de semana, amigo... Não tem RU não kkkk")

        breakfast_menu = ""

        for label in response['DESJEJUM']:
            dish = str('*' + label + '*' + ': ' + response['DESJEJUM'][label] + '\n')
            breakfast_menu += dish
        
        messages.append(breakfast_menu)

        data = requests.get(
            'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'
            .format(TELEGRAM_ACCESS_TOKEN, sender_id,'Eai! Então... Pro café da manhã, nós teremos: ')
        ).json()
        messenger = ""
        # Check if user data was get succefully
        if not data['ok']:
            messenger = "Facebook"
        else:
            messenger = "Telegram"

        for message in messages:

            if(messenger == "Telegram"):
                requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=Markdown'
                .format(TELEGRAM_ACCESS_TOKEN,sender_id, message))
            
        return []
