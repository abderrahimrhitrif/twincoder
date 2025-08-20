import subprocess

import subprocess
import threading

def run_command(command: str) -> dict:
    """
    Run a shell command. If interactive prompts appear, return them as 'prompts'
    for the chat loop to handle.
    """
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        output_lines = []
        prompts = []

        def read_output():
            for line in process.stdout:
                output_lines.append(line)
                print(line, end="")
                if "?" in line or "select" in line.lower():
                    prompts.append(line.strip())

        thread = threading.Thread(target=read_output)
        thread.start()
        process.wait()
        thread.join()

        return {
            "status": "completed",
            "output": "".join(output_lines),
            "prompts": prompts
        }
    except Exception as e:
        return {"status": "error", "output": str(e), "prompts": []}


tool = {
    "type": "function",
    "function": {
        "name": "run_command",
        "description": "Execute a shell command with user confirmation. You should not execute any interactive commands with this otherwise the shell hangs, use this when the other tools are not enought to fulfill the user query",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string"}
            },
            "required": ["command"]
        }
    }
}
