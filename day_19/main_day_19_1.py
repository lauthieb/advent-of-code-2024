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


def can_form_design(design, patterns):
    cache = {}

    def helper(remaining_design):
        if remaining_design in cache:
            return cache[remaining_design]
        if not remaining_design:
            return True

        for pattern in patterns:
            if remaining_design.startswith(pattern):
                if helper(remaining_design[len(pattern):]):
                    cache[remaining_design] = True
                    return True

        cache[remaining_design] = False
        return False

    return helper(design)


@measure_time
def count_possible_designs(input_file):
    with open(input_file, "r") as f:
        lines = f.read().strip().split("\n")

    patterns = lines[0].split(", ")
    designs = [line.strip() for line in lines[2:]]

    possible_count = 0
    for design in designs:
        if can_form_design(design, patterns):
            possible_count += 1

    return possible_count


if __name__ == "__main__":
    try:
        result = count_possible_designs(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
