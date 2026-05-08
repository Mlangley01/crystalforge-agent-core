from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel
from utils.json_parser import extract_json

FILE = "memory/research.xlsx"

HEADERS = [
    "idea_id", "summary", "problem_context", "relevant_technologies",
    "existing_solutions_competitors", "feasibility_assessment",
    "constraints_risks", "opportunities_angles",
    "recommendation", "suggested_next_agent", "notes"
]

def run(idea_card: dict) -> dict:
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    # --- Primary prompt ---
    prompt = f"""
You are the Research Agent.

Return ONLY a SINGLE JSON object.
No explanations. No markdown. No commentary. No code fences.

The JSON MUST contain exactly these keys:
{HEADERS}

IMPORTANT RULES:
- Every value MUST be a STRING.
- Do NOT return arrays, lists, objects, numbers, or booleans.
- If a field is unknown, return an empty string "".

Input:
{idea_card}

Return ONLY valid JSON:
"""

    # First attempt
    output = call_ollama("llama3", prompt)
    parsed = extract_json(output)

    # --- Retry with stricter prompt ---
    if parsed is None:
        strict_prompt = f"""
Return ONLY valid JSON. No text. No markdown. No commentary.

Keys:
{HEADERS}

Input:
{idea_card}
"""
        output = call_ollama("llama3", strict_prompt)
        parsed = extract_json(output)

    # --- If still no JSON, print raw output ---
    if parsed is None:
        print("RAW MODEL OUTPUT:")
        print(output)
        print("\n--- JSON PARSE FAILED ---\n")
        return {}

    # --- STRING-ONLY ENFORCEMENT ---
    for key in HEADERS:
        val = parsed.get(key, "")
        if not isinstance(val, str):
            parsed[key] = str(val)

    # --- Append to Excel ---
    df.loc[len(df)] = [parsed.get(h, "") for h in HEADERS]
    save_excel(FILE, df)

    return parsed
