from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel

FILE = "memory/mvp.xlsx"

HEADERS = [
    "idea_id", "product_overview", "target_user_problem",
    "core_use_cases", "mvp_feature_list", "non_goals",
    "technical_assumptions", "risks_mitigations",
    "phased_roadmap", "suggested_next_agent", "notes"
]

def run(discovery_pack: dict):
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    prompt = f"""
You are the MVP Architect Agent. Produce an MVP Spec for this idea:

{discovery_pack}

Return ONLY a JSON object with keys:
{HEADERS}
"""

    output = call_ollama("llama3", prompt)

    # TODO: parse JSON
    save_excel(FILE, df)
