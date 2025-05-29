from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionExplainCOD(Action):
    def name(self) -> Text:
        return "action_explain_cod"

    def run(self, dispatcher, tracker, domain):
    # your logic here
    dispatcher.utter_message("Explain COD..")
    return []
