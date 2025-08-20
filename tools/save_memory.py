def save_memory(fact: str) -> bool:
    with open("../memory.md", 'a') as memory:
        memory.write(f"{fact}\n")


tool = {
    "type": "function",
    "function": {
        "name": "save_memory",
        "description": "Saves a specific piece of information or fact to your long-term memory. Use this when the user explicitly asks you to remember something, or when they state a clear, concise fact that seems important to retain for future interactions.",
        "parameters": {
            "type": "object",
            "properties": {
                "fact": {
                    "type": "string",
                    "description": 'The specific fact or piece of information to remember. Should be a clear, self-contained statement.',
                        }
            },
            "required": ["fact"]
        }
    }
}
