from pathlib import Path
import re
from typing import Optional

def search_file_content(pattern: str, path: Optional[str] = None, include: Optional[str] = None) -> str:
    """
    Searches files for a regex pattern, optionally filtered by glob.
    Returns lines containing matches with file path and line numbers.
    """
    search_root = path if path else "."
    include_pattern = include if include else "**/*"
    matches = []
    for file_path in Path(search_root).rglob(include_pattern):
        if not file_path.is_file():
            continue
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, start=1):
                if re.search(pattern, line):
                    matches.append(f"File: {file_path}\nL{i}: {line.rstrip()}")
    return f"Found {len(matches)} matches for pattern '{pattern}' in path '{search_root}' (filter: '{include}'):\n---\n" + "\n---\n".join(matches)


tool = {
    "type": "function",
    "function": {
        "name": "search_file_content",
        "description": "Searches for a regex pattern within files. Can filter by glob pattern and returns matching lines with file paths and line numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Regex pattern to search for."},
                "path": {"type": "string", "description": "Directory to search within."},
                "include": {"type": "string", "description": "Glob pattern to filter which files are searched."}
            },
            "required": ["pattern"]
        }
    }
}