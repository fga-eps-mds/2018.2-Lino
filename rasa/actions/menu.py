import requests
import time
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

class ActionDailyMenu(Action):
    def name(self):
        return "action_daily_menu"
    
    def run(self, dispatcher, tracker, domain):
        messages = []
        period = tracker.get_slot('period')
        meal = tracker.get_slot('meal')
        day = time.strftime('%A',time.localtime())
        response = requests.get(
            f'https://webcrawler-ru.lappis.rocks/cardapio/{day}').json()
        messages.append('Olá! Para o café de hoje nós teremos: ')
        for label in response['DESJEJUM']:
            messages.append(label + ' ' + response['DESJEJUM'][label])
        messages.append('Para o almoço nós teremos: ')    
        for label in response['ALMOÇO']:
            messages.append(label + ' ' + response['ALMOÇO'][label])
        messages.append('Para o jantar nós teremos: ')
        for label in response['JANTAR']:
            messages.append(label + ' ' + response['JANTAR'][label])
        for message in messages:
            dispatcher.utter_message(message)
        return []

class ActionWeeklyMenu(Action):
    def name(self):
        return "action_weekly_menu"
    
    def run(self, dispatcher, tracker, domain):
        pass

class ActionNextMeal(Action):
    def name(self):
        return "action_next_meal"
    
    def run(self, dispatcher, tracker, domain):
        pass
