import requests
import time
from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted

class ActionDailyMenu(Action):
    def name(self):
        return "action_daily_menu"
    
    def run(self, dispatcher, tracker, domain):
        period = tracker.get_slot('period')
        meal = tracker.get_slot('meal')
        day = time.strftime('%A',time.localtime())
        response = requests.get(
            f'https://3cbf5110.ngrok.io/cardapio/{day}').json()
        print(period)
        dispatcher.utter_message(response['ALMOÇO'])
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
