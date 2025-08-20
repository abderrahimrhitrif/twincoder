from pathlib import Path

def replace(file_path: str, old_string: str, new_string: str, expected_replacements: int = 1) -> str:
    """
    Replaces text within a file. Can create new files if old_string is empty.
    """
    p = Path(file_path)
    if old_string == "":
        if p.exists():
            return f"Failed: file {file_path} already exists."
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(new_string, encoding="utf-8")
        return f"Created new file: {file_path} with provided content."
    
    if not p.exists():
        return f"Failed: file {file_path} does not exist."
    
    content = p.read_text(encoding="utf-8")
    count = content.count(old_string)
    if count != expected_replacements:
        return f"Failed to edit, expected {expected_replacements} occurrences but found {count}."
    
    content = content.replace(old_string, new_string, expected_replacements)
    p.write_text(content, encoding="utf-8")
    return f"Successfully modified file: {file_path} ({expected_replacements} replacements)."

tool = {
    "type": "function",
    "function": {
        "name": "replace",
        "description": "Replaces text in a file. Requires exact old_string context and can create a new file if old_string is empty. Shows diff and requests confirmation.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Absolute path to the file to modify."},
                "old_string": {"type": "string", "description": "Exact literal text to replace (must include surrounding context)."},
                "new_string": {"type": "string", "description": "Text to replace old_string with."},
                "expected_replacements": {"type": "number", "description": "Number of occurrences to replace (default: 1)."}
            },
            "required": ["file_path", "old_string", "new_string"]
        }
    }
}