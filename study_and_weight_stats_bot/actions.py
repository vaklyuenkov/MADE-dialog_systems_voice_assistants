# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionContextDate(Action):

    def name(self) -> Text:
        return "action_context_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #get previous action name
        def get_latest_event(events):
            latest_actions = []
            for e in events:
                if e['event'] == 'action':
                    latest_actions.append(e)

            return latest_actions[-2:][0]['name']

        previous_action = get_latest_event(tracker.events)
        #get date
        date = tracker.get_slot('date')

        if previous_action == 'utter_weather_outfit':
            outfit = tracker.get_slot('outfit')
            reply = "Let me check for {} for {}".format(outfit,date)
        elif previous_action == 'utter_weather_condition':
            condition = tracker.get_slot('condition')
            reply = "Let me check for {} for {}".format(condition, date)
        elif previous_action == 'utter_weather_get':
            location = tracker.get_slot('location')
            reply = "Let me check for {} in {}".format(date, location)
        elif previous_action == 'utter_weather_activity':
            activity = tracker.get_slot('activity')
            reply = "Let me check for {} for {}".format(activity, date)
        else:
            reply = "Sorry, I don't understand"

        dispatcher.utter_message(text=reply)

        return []
