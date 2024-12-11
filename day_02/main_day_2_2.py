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


def generate_subsets(report):
    return [report[:i] + report[i + 1:] for i in range(len(report))]


def is_safe(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


@measure_time
def calculate_safe_count(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    safe_count = 0
    for line in lines:
        levels = list(map(int, line.strip().split()))

        if is_safe(levels):
            safe_count += 1
        else:
            for subset in generate_subsets(levels):
                if is_safe(subset):
                    safe_count += 1
                    break

    return safe_count


if __name__ == "__main__":
    try:
        result = calculate_safe_count(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
    else:
        sys.exit(0)