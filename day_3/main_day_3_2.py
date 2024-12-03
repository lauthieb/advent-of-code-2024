import sys
import os
import re

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


@measure_time
def get_multiply(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    total_sum = 0
    operations = []

    for line in lines:
        matches = re.findall(pattern, line)
        operations.extend(matches)

    should_take_mul = True

    for operation in operations:
        if operation.startswith("mul") and should_take_mul:
            numbers = re.search(r"\((\d{1,3}),(\d{1,3})\)", operation)
            if numbers:
                a, b = int(numbers.group(1)), int(numbers.group(2))
                total_sum += a * b
        elif operation == "don't()":
            should_take_mul = False
        elif operation == "do()":
            should_take_mul = True

    return total_sum


if __name__ == "__main__":
    try:
        result = get_multiply(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
