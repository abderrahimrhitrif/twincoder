from core.chat import get_response

def interactive_shell(selected_model):
    print(f"\nEntering shell for model: {selected_model}")
    print("Type something and press Enter (type '/exit' to quit):\n")

    while True:
        try:
            user_input = input(">> ")
            if user_input.lower() in ("/exit", "/quit"):
                print("Exiting shell...")
                break
            get_response(user_input, selected_model)
        except KeyboardInterrupt:
            print("\nExiting shell...")
            break
