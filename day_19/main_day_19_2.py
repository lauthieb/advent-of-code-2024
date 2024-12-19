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


def count_ways_to_form_design(design, patterns):
    cache = {}

    def count_ways(remaining_design):
        if remaining_design in cache:
            return cache[remaining_design]
        if not remaining_design:
            return 1
        total_ways = 0
        for pattern in patterns:
            if remaining_design.startswith(pattern):
                total_ways += count_ways(remaining_design[len(pattern):])

        cache[remaining_design] = total_ways
        return total_ways

    return count_ways(design)


@measure_time
def sum_all_possible_ways(input_file):
    with open(input_file, "r") as f:
        lines = f.read().strip().split("\n")

    patterns = lines[0].split(", ")
    designs = [line.strip() for line in lines[2:]]

    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(design, patterns)

    return total_ways


if __name__ == "__main__":
    try:
        result = sum_all_possible_ways(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
