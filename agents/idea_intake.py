import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.ollama_client import call_ollama
from utils.excel_utils import ensure_excel, load_excel, save_excel
from utils.json_parser import extract_json

FILE = "memory/ideas.xlsx"

HEADERS = [
    "id", "title", "raw_input", "category", "description",
    "assumptions", "unknowns", "risks", "dependencies",
    "impact_score", "feasibility_score", "alignment_score",
    "novelty_score", "urgency_score", "total_weighted_score",
    "status", "current_owner_agent", "notes"
]

def run(raw_idea: str) -> dict:
    ensure_excel(FILE, HEADERS)
    df = load_excel(FILE)

    # --- Primary prompt ---
    prompt = f"""
You are the Idea Intake Agent.

Return ONLY a SINGLE JSON object.
No explanations. No markdown. No commentary. No code fences.

The JSON MUST contain exactly these keys:
{HEADERS}

IMPORTANT RULES:
- Every value MUST be a STRING.
- Do NOT return arrays, lists, objects, numbers, or booleans.
- If a field is unknown, return an empty string "".

Input:
{raw_idea}

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
{raw_idea}
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
