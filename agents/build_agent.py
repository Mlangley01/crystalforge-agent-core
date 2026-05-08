from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel

FILE = "memory/build.xlsx"

HEADERS = [
    "idea_id", "code_or_architecture", "implementation_notes",
    "testing_suggestions", "open_questions",
    "suggested_next_agent", "notes"
]

def run(execution_plan: dict):
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    prompt = f"""
You are the Build Agent. Produce a Build Artefact Pack for this task:

{execution_plan}

Return ONLY a JSON object with keys:
{HEADERS}
"""

    output = call_ollama("llama3", prompt)

    # TODO: parse JSON
    save_excel(FILE, df)
