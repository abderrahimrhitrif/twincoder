# TwinCoder — Local AI Coding Assistant

## Overview
TwinCoder is a locally-run AI coding assistant operating directly within the terminal, powered by Ollama. It provides a private, secure, and customizable coding experience with file system operations and tool execution capabilities.

## Architecture & Pipeline
1. **Interactive CLI (`cli/`)**: Rich terminal interface handling user input, alternate screen buffers, and styled rendering.
2. **Core Agent (`core/`)**: Manages chat completion loops, tool dispatching, and conversation context.
3. **Extensible Tools (`tools/`)**: Modular toolset allowing the AI agent to read files, write files, search file content, list directories, run shell commands, and save memory.
4. **Ollama Service (`services/`)**: OpenAI-compatible client connection interfacing directly with local Ollama models.

## Data
- **Source**: Local project file directories and user terminal prompts.

## Method & Algorithms
- **Agentic Tool Calling**: Function calling loop supporting file inspection, replacement, shell execution, and memory persistence.

## Verified Results & Metrics
- Built modular terminal assistant supporting secure local LLM inference, file system tool execution, and interactive CLI rendering.

## Limitations & Caveats
- Personal developer productivity tool; requires local Ollama instance running.

## Run Instructions
```bash
pip install -r requirements.txt
python main.py
```

## Claims to Avoid
- Do not claim commercial AI coding assistant user base or enterprise IDE distribution.
