import sys

def enter_alternate_screen():
    sys.stdout.write("\033[?1049h")
    sys.stdout.flush()

def exit_alternate_screen():
    sys.stdout.write("\033[?1049l")
    sys.stdout.flush()

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def diagonal_gradient_text(text, start_color, end_color):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines) if lines else 0
    gradient_lines = []
    for i, line in enumerate(lines):
        colored_chars = []
        for j, char in enumerate(line):
            ratio = ((i / max(1, height - 1)) + (j / max(1, width - 1))) / 2
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            colored_chars.append(f"{rgb_to_ansi(r, g, b)}{char}\033[0m")
        gradient_lines.append("".join(colored_chars))
    return "\n".join(gradient_lines)
