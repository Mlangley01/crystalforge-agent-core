from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel

FILE = "memory/discovery.xlsx"

HEADERS = [
    "idea_id", "target_persona", "key_pain_points", "customer_language",
    "objections", "signals_of_demand", "fit_score",
    "recommendation", "suggested_next_agent", "notes"
]

def run(idea_card: dict):
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    prompt = f"""
You are the Customer Discovery Agent. Produce a Discovery Insight Pack for this idea:

{idea_card}

Return ONLY a JSON object with keys:
{HEADERS}
"""

    output = call_ollama("llama3", prompt)

    # TODO: parse JSON
    save_excel(FILE, df)
