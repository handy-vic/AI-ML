from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import re
from datetime import datetime


class ActionGetTopDelays(Action):
    
    def name(self) -> Text:
        return "action_get_top_delays"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Load your cleaned data file (CSV preferred)
        try:

            # Load the text file
            file_path = "./log/delay_log.txt"
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Pattern to match delay entries with arrival (AT), departure (OUT), and cause (COD)
            pattern = re.compile(
                r"(?P<date>\d{1,2}/\d{1,2}/\d{4})?\s*WITS\s+\d+\s+(?P<station>[A-Z]{3})\s*[\s\S]*?AT\s*:\s*(?P<at>\d{3,4})\s*OUT\s*(?P<out>\d{3,4})\s*HRS[\s\S]*?(?:COD|Cod|cod)\s*[:]*\s*(?P<cod>.*?)(?=\n|$)",
                re.IGNORECASE
            )

            # Extract matches
            matches = pattern.finditer(text)

            # Process extracted data
            records = []
            for match in matches:
                date = match.group("date") or ""
                station = match.group("station")
                at_time = match.group("at")
                out_time = match.group("out")
                cod = match.group("cod").strip()

                # Convert AT and OUT to HH:MM format
                def format_time(t):
                    t = t.zfill(4)
                    return f"{t[:2]}:{t[2:]}"

                at_formatted = format_time(at_time)
                out_formatted = format_time(out_time)

                records.append({
                    "Date": date,
                    "Station": station,
                    "AT": at_formatted,
                    "OUT": out_formatted,
                    "Cause of Delay": cod
                })

            # Create DataFrame
            df = pd.DataFrame(records)

            # # # Save to CSV
            # csv_path = "/mnt/data/train_delay_log.csv"
            # df.to_csv(csv_path, index=False)
            # df = pd.read_csv(csv_path)


        except Exception as e:
            dispatcher.utter_message(f"Error loading data: {e}")
            return []

        df["delay_minutes"] = pd.to_datetime(df["OUT"]) - pd.to_datetime(df["AT"])
        df["delay_minutes"] = df["delay_minutes"].dt.total_seconds() / 60
        df = df.sort_values("delay_minutes", ascending=False)

        top = df.head(5)[["Date", "Station", "AT", "OUT", "delay_minutes", "COD"]]

        msg = "📊 Top 5 Longest Delays:\n"
        for i, row in top.iterrows():
            msg += f"\n{row['Date']} — {row['Station']}\n⏱ {int(row['delay_minutes'])} mins\n🔧 {row['COD']}\n"

        dispatcher.utter_message(msg)
        return []