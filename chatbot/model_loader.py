import subprocess

model: str = "llama3.2"

def run_ollama(prompt: str):
    try:
        command = ["ollama", "run", model]

        process = subprocess.run(
            command,
            input=prompt,
            text=True,
            capture_output=True,
            encoding='utf-8'  # Explicitly set UTF-8 encoding
        )
        if process.returncode == 0:
            return process.stdout.strip()
        else:
            return {"error": process.stderr.strip()}
    except Exception as e:
        return {"error": str(e)}