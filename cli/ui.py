from config import logo, start_color, end_color
from core.utils import diagonal_gradient_text
import sys

def show_logo():
    sys.stdout.write("\033[H")  # Move cursor home
    print(diagonal_gradient_text(logo, start_color, end_color))
