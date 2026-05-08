from utils.ollama_client import call_ollama

def run(founder_report: dict):
    prompt = f"""
You are the Founder Profile Agent. Produce:
- 3 LinkedIn post drafts
- 3 profile improvements
- 3 content themes

Input:
{founder_report}

Return plain text.
"""

    output = call_ollama("llama3", prompt)
    return output
