# Building an AI Assistant using Rasa for your railway delay monitoring
📁 NLU Training Data
Intents: query_top_delays, station_report, suggest_fix, explain_cod, etc.
Entities: station, month, date, COD type, loco number

🧠 Core (Stories / Rules) : nlu.yml, stories.yml, rules.yml
User flows: greeting → query → data fetch → suggestion

⚙️ Custom Actions (Python SDK) : reports.py, suggesstions.py, topdelays.py, validators.py
Logic like top delay calculation or filtering by date/station

🗂 Backend Data: CSV
Train movements, delays and causes (CSV)

🎛 UI / Chat Interface:
To be integrate with Python UI dashboard (Lastly)
