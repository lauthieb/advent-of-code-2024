import sys
import os

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


@measure_time
def count_total_calibration(input_file):
    from itertools import product

    total = 0

    def sum_search(inputs, temp):
        result = []
        left = inputs.pop(0)
        for value in temp:
            result.append(left + value)
            result.append(left * value)

        if len(inputs) > 0:
            result = sum_search(inputs=inputs, temp=result)
        return result

    with open(input_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))

        temp = []
        temp.append(numbers.pop(0))
        if test_value in sum_search(inputs=numbers, temp=temp):
            total += test_value

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
