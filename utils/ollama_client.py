import subprocess

def call_ollama(model: str, prompt: str) -> str:
    """Call a local Ollama model and return the raw output."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")
