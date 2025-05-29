from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionReports(Action):
    def name(self) -> Text:
        return "action_station_reports"

    def run(self, dispatcher, tracker, domain):
    # your logic here
    dispatcher.utter_message("Reports from stations, month, date..")
    return []
