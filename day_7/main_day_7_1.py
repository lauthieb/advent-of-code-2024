import sys
import os

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


@measure_time
def count_total_calibration(input_file):
    from itertools import product

    total = 0

    with open(input_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))

        num_operators = len(numbers) - 1
        operator_combinations = product("+*", repeat=num_operators)

        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total += test_value
                break

    return total


if __name__ == "__main__":
    try:
        result = count_total_calibration(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
