import random
import sys
import time
import os

# ANSI color codes
COLOR_CODES = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'  # Reset color to default
}

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def move_cursor(x, y):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def matrix_effect(width, height):
    while True:
        clear_screen()
        for y in range(1, height + 1):
            line = ''
            for x in range(1, width + 1):
                if random.random() < 0.1:
                    color = random.choice(list(COLOR_CODES.values())[:-1])  # Exclude reset color
                    symbol = random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    line += f"{color}{symbol}{COLOR_CODES['reset']}"
                else:
                    line += ' '
            sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.1)

try:
    _, columns = os.popen('stty size', 'r').read().split()
    width, height = int(columns), 40  # Adjust height as needed
except:
    width, height = 120, 40  # Default values if unable to get terminal size
matrix_effect(500, 240)
