# Rasa Architecture
📁 NLU Training Data

Intents: query_top_delays, station_report, suggest_fix, explain_cod, etc.

Entities: station, month, date, COD type, loco number

🧠 Core (Stories / Rules)

Define user flows: greeting → query → data fetch → suggestion

⚙️ Custom Actions (Python SDK)

Parse and analyze your data file (e.g., .txt or .csv)

Run logic like top delay calculation or filtering by date/station

🗂 Backend Data

Ideally pre-process your logs into structured format (JSON, CSV, SQLite, etc.)

Alternatively, use Pandas to parse the .txt logs directly in your custom actions

🎛 UI / Chat Interface

Web widget (Rasa Webchat, Botfront, Streamlit)

Integrate with dashboards if desired
