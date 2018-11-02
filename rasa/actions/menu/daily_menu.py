import requests
import time
from rasa_core.actions.action import Action


class ActionDailyMenu(Action):
    def name(self):
        return "action_daily_menu"

    def run(self, dispatcher, tracker, domain):
        messages = []

        day = time.strftime('%A', time.localtime())

        # Change the url if you have your own webcrawler server
        response = requests.get(
            'http://webcrawler-ru.lappis.rocks/cardapio/{}'
            .format(day)
        ).json()

        messages.append('Eai! Então... Pro café da manhã, nós teremos: ')

        breakfast_block = ""

        for label in response['DESJEJUM']:
            cell = str(label + ': ' + response['DESJEJUM'][label] + '\n')
            breakfast_block += cell

        messages.append(breakfast_block)

        messages.append('Já, para o almoço, teremos: ')

        lunch_block = ""

        for label in response['ALMOÇO']:
            cell = str(label + ' ' + response['ALMOÇO'][label] + '\n')
            lunch_block += cell

        messages.append(lunch_block)

        messages.append('E para a janta...')

        dinner_block = ""

        for label in response['JANTAR']:
            cell = str(label + ' ' + response['JANTAR'][label] + '\n')
            dinner_block += cell

        messages.append(dinner_block)

        for message in messages:
            dispatcher.utter_message(message)

        return []


class ActionNextMeal(Action):
    def name(self):
        return "action_next_meal"

    def run(self, dispatcher, tracker, domain):
        pass
