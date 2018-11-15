from rasa_core.actions.action import Action
from rasa_core.events import UserUttered


class ActionTriggerNotification(Action):
    def name(self):
        return "action_another_notification"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('TA BOM MANO')
        tracker.update(
            UserUttered('Me manda notificações',
                        intent={
                            'name': 'asks_about_register_notifications',
                            'confidence': 1.0}))
        return []

class ActionTriggerUnregisterNotification(Action):
    def name(self):
        return "action_trigger_unregister_notification"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('BELEZA VEI')

        tracker.update(
            UserUttered(
                'sem notificações',
                intent={
                    'name': 'asks_about_unregister_notification',
                    'confidence': 1.0
                }
            )
        )

        return []
