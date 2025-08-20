import glob as glob_module
from typing import Optional
import os

def search_file(pattern: str, path: Optional[str] = None, case_sensitive: bool = False, respect_git_ignore: bool = True) -> str:
    """
    Finds files matching a glob pattern, sorted by modification time (newest first).
    """
    root = path if path else "."
    files = glob_module.glob(os.path.join(root, pattern), recursive=True)
    files = [f for f in files if os.path.isfile(f)]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    output = f"Found {len(files)} file(s) matching '{pattern}' within {root}:\n"
    output += "\n".join(files)
    return output

tool = {
    "type": "function",
    "function": {
        "name": "search_file",
        "description": "Finds files matching a glob pattern, optionally filtered by directory. Sorted by modification time (newest first).",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Glob pattern to match files."},
                "path": {"type": "string", "description": "Directory to search within."},
                "case_sensitive": {"type": "boolean", "description": "Whether the search is case-sensitive."},
                "respect_git_ignore": {"type": "boolean", "description": "Whether to respect .gitignore patterns."}
            },
            "required": ["pattern"]
        }
    }
}