from typing import Dict, Text, Any, List
from rasa_sdk import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ValidateDelayQueryForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_delay_query_form"

    def validate_station(self, slot_value: Any, dispatcher, tracker, domain: DomainDict) -> Dict[Text, Any]:
        # Add your logic to validate known stations
        known_stations = ["JEV","ABO","PAR","ARK","BOR","HEN","GBO","ATA","ROM","NED","IPE","NKE"]
        if slot_value.upper() in known_stations:
            return {"station": slot_value.upper()}
        dispatcher.utter_message(text="Sorry, I didn’t recognize that station.")
        return {"station": None}

    def validate_date(
        self, slot_value: Any, dispatcher, tracker, domain: DomainDict
    ) -> Dict[Text, Any]:
        # Optionally validate the date format
        return {"date": slot_value}
