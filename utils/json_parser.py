import json
import re

def extract_json(text: str):
    """
    Extract the first valid JSON object from a model's output.
    Handles:
    - Markdown code fences
    - Extra commentary before/after JSON
    - Multiple JSON blocks
    - Imperfect formatting
    """

    # 1. Try direct JSON first
    try:
        return json.loads(text)
    except:
        pass

    # 2. Try to extract JSON inside code fences
    fence_match = re.search(r"```(?:json)?(.*?)```", text, re.DOTALL)
    if fence_match:
        candidate = fence_match.group(1).strip()
        try:
            return json.loads(candidate)
        except:
            pass

    # 3. Try to extract the first {...} block
    brace_match = re.search(r"\{.*\}", text, re.DOTALL)
    if brace_match:
        candidate = brace_match.group(0)
        try:
            return json.loads(candidate)
        except:
            pass

    # 4. If everything fails, return None
    return None
