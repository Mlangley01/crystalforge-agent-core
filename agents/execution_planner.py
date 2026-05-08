from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel

FILE = "memory/execution.xlsx"

HEADERS = [
    "idea_id", "cycle_goal", "milestones", "tasks",
    "schedule_by_block", "dependencies_risks",
    "suggested_next_agent", "notes"
]

def run(mvp_spec: dict):
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    prompt = f"""
You are the Execution Planner Agent. Produce an Execution Plan for this MVP:

{mvp_spec}

Return ONLY a JSON object with keys:
{HEADERS}
"""

    output = call_ollama("llama3", prompt)

    # TODO: parse JSON
    save_excel(FILE, df)
