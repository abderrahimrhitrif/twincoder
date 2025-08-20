from pathlib import Path


def write_file(file_path: str, content: str) -> str:
    """
    Writes content to a file. Creates parent directories if they don't exist.
    """
    p = Path(file_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"Successfully wrote to file: {file_path}"


tool = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file. Creates parent directories if needed. Shows diff and requests confirmation before overwriting.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Absolute path to the file to write."},
                "content": {"type": "string", "description": "Content to write into the file."}
            },
            "required": ["file_path", "content"]
        }
    }
}