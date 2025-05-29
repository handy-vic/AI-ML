from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionSuggest(Action):
    def name(self) -> Text:
        return "action_suggest_fix"

    def run(self, dispatcher, tracker, domain):
    # your logic here
    dispatcher.utter_message("LLM to suggest fix..")
    return []
