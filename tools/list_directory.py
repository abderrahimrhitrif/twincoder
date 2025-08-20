from pathlib import Path
from typing import List, Optional

def list_directory(path: str, ignore: Optional[List[str]] = None, respect_git_ignore: bool = True) -> str:
    """
    Lists files and directories in the given path.
    Directories appear first, then files, sorted alphabetically.
    """
    p = Path(path)
    if not p.is_dir():
        return f"Error: {path} is not a directory."
    
    entries = []
    for entry in p.iterdir():
        if ignore and any(Path(entry.name).match(pattern) for pattern in ignore):
            continue
        entries.append(entry)
    
    dirs = sorted([e.name for e in entries if e.is_dir()])
    files = sorted([e.name for e in entries if not e.is_dir()])
    output = f"Directory listing for {path}:\n"
    output += "\n".join([f"[DIR] {d}" for d in dirs] + files)
    return output

tool = {
    "type": "function",
    "function": {
        "name": "list_directory",
        "description": "Lists files and directories in a specified directory path. Directories appear first, then files, sorted alphabetically.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute path to the directory to list."},
                "ignore": {"type": "array", "items": {"type": "string"}, "description": "List of glob patterns to ignore."},
                "respect_git_ignore": {"type": "boolean", "description": "Whether to respect .gitignore patterns."}
            },
            "required": ["path"]
        }
    }
}