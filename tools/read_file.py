from pathlib import Path
from typing import Optional, Union
import base64

def read_file(path: str, offset: Optional[int] = None, limit: Optional[int] = None) -> Union[str, dict]:
    """
    Reads text files (with optional line slicing), images, PDFs, and handles binary files.
    """
    p = Path(path)
    if not p.is_file():
        return f"Error: {path} is not a file."
    
    ext = p.suffix.lower()
    text_extensions = {".txt", ".py", ".ts", ".js", ".json", ".md"}
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"}
    pdf_extensions = {".pdf"}

    if ext in text_extensions:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        total_lines = len(lines)
        start = offset if offset else 0
        end = start + limit if limit else total_lines
        truncated = end < total_lines
        content_lines = lines[start:end]
        prefix = f"[File content truncated: showing lines {start + 1}-{min(end, total_lines)} of {total_lines} total lines...]\n" if truncated else ""
        return prefix + "".join(content_lines)
    
    elif ext in image_extensions or ext in pdf_extensions:
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        mime_type = "application/pdf" if ext in pdf_extensions else f"image/{ext[1:]}"
        return {"inlineData": {"mimeType": mime_type, "data": data}}
    
    else:
        return f"Cannot display content of binary file: {path}"
    
tool = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Reads a file's content. Supports text, images, PDFs, and handles binary files.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute path to the file to read."},
                "offset": {"type": "number", "description": "Line number to start reading from (text files only)."},
                "limit": {"type": "number", "description": "Maximum number of lines to read (text files only)."}
            },
            "required": ["path"]
        }
    }
}