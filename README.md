# TwinCoder - Your Local AI Coding Companion

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

TwinCoder is a powerful, locally-run AI coding assistant that operates directly within your terminal. It leverages the capabilities of local LLMs through Ollama to provide a private, secure, and highly customizable coding experience.

## 🚀 About The Project

TwinCoder is designed for developers who value privacy and want to harness the power of AI without sending their code to third-party servers. By running on your local machine, it offers a sandboxed environment for code generation, analysis, and tool utilization.

**Key Features:**

*   **Interactive Chat:** Engage in a dialogue with your AI assistant to ask questions, get code snippets, and brainstorm ideas.
*   **File System Operations:** Grant the AI the ability to read, write, and list files, enabling it to understand and modify your codebase directly.
*   **Command Execution:** Allow the AI to run shell commands, automating tasks like running tests, installing dependencies, or executing scripts.
*   **Extensible Toolset:** The agent's capabilities can be expanded with new tools to meet the specific demands of your projects.
*   **Local First:** Powered by Ollama, all processing happens on your machine, ensuring your data stays private.

## 🛠️ Getting Started

Follow these steps to get your local instance of TwinCoder up and running.

### Prerequisites

*   **Python 3.11+**
*   **Ollama:** Ensure Ollama is installed and running. You can download it from [ollama.ai](https://ollama.ai/).
    *   You will also need to have a model pulled, for example: `ollama pull llama3`

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your_username/twincoder.git
    cd twincoder
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    Modify the `config.py` file to set your preferred Ollama model and other settings.

## 🏃‍♀️ Usage

To start the TwinCoder assistant, run the main script:

```sh
python main.py
```

This will launch the interactive CLI where you can start conversing with the AI.

## 🏗️ Project Structure

*   `main.py`: The entry point for the application.
*   `config.py`: Main configuration file for models and other settings.
*   `cli/`: Handles the command-line interface, user input, and UI rendering.
*   `core/`: Contains the core chat logic and agent orchestration.
*   `services/`: Includes clients for interacting with external services like Ollama.
*   `tools/`: Defines the tools that the AI agent can use (e.g., `read_file`, `run_command`).

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

*   [Ollama](https://ollama.ai/)
*   [Python](https://www.python.org/)
