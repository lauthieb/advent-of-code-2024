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


@measure_time
def calculate_sum_each_buyer(input_file):
    with open(input_file, "r") as f:
        lines = list(map(int, f.readlines()))
        results = []

        for line in lines:
            for _ in range(2000):
                line = ((line * 64) ^ line) % 16777216
                line = ((line // 32) ^ line) % 16777216
                line = ((line * 2048) ^ line) % 16777216
            results.append(line)

        return sum(results)


if __name__ == "__main__":
    try:
        result = calculate_sum_each_buyer(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
