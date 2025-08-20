import subprocess

def get_models():
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    output = result.stdout
    lines = output.strip().split("\n")[1:]  # Skip header
    return [line.split()[0] for line in lines]
