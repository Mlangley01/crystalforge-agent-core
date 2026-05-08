from utils.ollama_client import call_ollama

def run(all_data: dict):
    prompt = f"""
You are the Founder Ops Agent. Produce a weekly Founder Report.

Input data:
{all_data}

Return plain text.
"""

    output = call_ollama("llama3", prompt)
    return output
