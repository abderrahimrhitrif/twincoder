import json
from time import sleep
from services.ollama_client import client
from tools import tools, tool_functions

with open("memory.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

def handle_tool_calls(tool_calls, model):
    tool_messages = []

    for tool_call in tool_calls:
        function_name = tool_call["function"]["name"]
        handler = tool_functions.get(function_name)

        if not handler:
            result = {
                "status": "error",
                "output": f"Unknown function: {function_name}",
                "prompts": []
            }
        else:
            try:
                args = json.loads(tool_call["function"]["arguments"])
                result = handler(**args)
            except json.JSONDecodeError:
                # fallback if args is a plain string
                result = handler(tool_call["function"]["arguments"])

        # 🔄 Loop until no more interactive prompts
        while isinstance(result, dict) and result.get("prompts"):
            for prompt in result["prompts"]:
                # Ask the LLM how to respond to the prompt
                answer = get_response(prompt, model)

                # Re-run the tool with the provided input
                if isinstance(args, dict):
                    args["user_input"] = answer.strip()
                else:
                    args = {"command": args, "user_input": answer.strip()}

                result = handler(**args)

        tool_messages.append({
            "role": "tool",
            "tool_call_id": tool_call["id"],
            "content": json.dumps(result) if isinstance(result, dict) else str(result)
        })

    messages.extend(tool_messages)

    # Continue chat after tool execution
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        stream=True
    )

    full_content = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            content_piece = chunk.choices[0].delta.content
            full_content += content_piece
            print(content_piece, end="", flush=True)
            sleep(0.01)

    print()
    if full_content:
        messages.append({"role": "assistant", "content": full_content})
    return full_content


def get_response(message, model):
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        stream=True
    )

    full_content = ""
    tool_calls = []
    current_tool_call = None

    for chunk in response:
        if chunk.choices[0].delta.content:
            content_piece = chunk.choices[0].delta.content
            full_content += content_piece
            print(content_piece, end="", flush=True)
            sleep(0.01)

        if hasattr(chunk.choices[0].delta, "tool_calls") and chunk.choices[0].delta.tool_calls:
            for tool_call_delta in chunk.choices[0].delta.tool_calls:
                if tool_call_delta.id:
                    current_tool_call = {
                        "id": tool_call_delta.id,
                        "function": {"name": "", "arguments": ""}
                    }
                    tool_calls.append(current_tool_call)
                if current_tool_call and tool_call_delta.function:
                    if tool_call_delta.function.name:
                        current_tool_call["function"]["name"] = tool_call_delta.function.name
                    if tool_call_delta.function.arguments:
                        current_tool_call["function"]["arguments"] += tool_call_delta.function.arguments

    print()
    assistant_message = {"role": "assistant", "content": full_content}
    if tool_calls:
        assistant_message["tool_calls"] = tool_calls
    messages.append(assistant_message)

    if tool_calls:
        handle_tool_calls(tool_calls, model)

    return full_content
