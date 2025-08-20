from cli.ui import show_logo
from cli.models import get_models
from cli.shell import interactive_shell
from core.utils import enter_alternate_screen, exit_alternate_screen
import questionary
from config import custom_style

def main():
    try:
        enter_alternate_screen()
        show_logo()
        models = get_models()
        if not models:
            print("No models available.")
            return

        selected_model = questionary.select(
            "Select a model:",
            choices=models,
            style=custom_style
        ).ask()

        if selected_model:
            print(f"You selected: {selected_model}")
            interactive_shell(selected_model)
        else:
            print("No selection made.")

    finally:
        exit_alternate_screen()

if __name__ == "__main__":
    main()
