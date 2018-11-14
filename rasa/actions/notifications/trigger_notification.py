from rasa_core.actions.action import Action
from rasa_core.events import UserUttered


class ActionTriggerNotification(Action):
    def name(self):
        return "action_another_notification"

    def run(self, dispatcher, tracker, domain):
        return [
            UserUttered("E as notificações",
                        intent={
                            'name': 'asks_about_notifications',
                            'confidence': 1.0
                        })
        ]
