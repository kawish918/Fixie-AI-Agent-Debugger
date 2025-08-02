# core/llama_interface.py
import subprocess

def query_llama(prompt, model="llama3.2"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30  # Add timeout
        )
        if result.returncode != 0:
            raise Exception(f"Ollama error: {result.stderr.decode('utf-8')}")
        return result.stdout.decode('utf-8')
    except Exception as e:
        return f"Error querying model: {str(e)}"