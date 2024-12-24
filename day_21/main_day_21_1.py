"""
INFO: I struggled a lot for this one.
After two days of reflection, I finally found and understood
an answer from the community here:
https://github.com/LiquidFun/adventofcode/blob/main/2024/21/21.py

Thanks a lot to @LiquidFun for sharing this.
This solution leverages complex numbers to model keypad positions,
making movement calculations simple and efficient.
It uses recursion with memoization to simulate nested commands and compute
the minimal sequence of button presses.
"""

import sys
import os
from functools import cache

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")
NUMERIC_KEYPAD = {
    "7": 0,
    "8": 1,
    "9": 2,
    "4": 1j,
    "5": 1+1j,
    "6": 2+1j,
    "1": 2j,
    "2": 1+2j,
    "3": 2+2j,
    " ": 3j,
    "0": 1+3j,
    "A": 2+3j
}
DIRECTIONAL_KEYPAD = {
    " ": 0,
    "^": 1,
    "A": 2,
    "<": 1j,
    "v": 1+1j,
    ">": 2+1j
}


@cache
def path(start, end):
    """
    This function calculates the shortest sequence of moves to navigate
    from one button (start) to another (end) on the appropriate keypad.
    """
    pad = NUMERIC_KEYPAD \
        if (start in NUMERIC_KEYPAD and end in NUMERIC_KEYPAD) \
        else DIRECTIONAL_KEYPAD
    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)
    yy = ("^"*-dy) + ("v"*dy)
    xx = ("<"*-dx) + (">"*dx)

    bad = pad[" "] - pad[start]
    prefer_yy_first = (dx > 0 or bad == dx) and bad != dy*1j
    return (yy+xx if prefer_yy_first else xx+yy) + "A"


@cache
def length(code, depth, s=0):
    """
    This recursive function calculates the total number of
    button presses required to type a code.
    """
    if depth == 0:
        return len(code)
    for i, c in enumerate(code):
        s += length(path(code[i-1], c), depth-1)
    return s


@measure_time
def calculate_sum_complexities(input_file):
    with open(input_file, "r") as f:
        codes = list(map(str.strip, f.readlines()))
        return sum(int(code[:-1]) * length(code, 3) for code in codes)


if __name__ == "__main__":
    try:
        result = calculate_sum_complexities(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
