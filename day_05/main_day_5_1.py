import sys
import os
from collections import defaultdict

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
def count_middle_page_number(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    rules = []
    updates = []

    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.strip().split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.strip().split(","))))

    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)

    def is_valid(update):
        position = {page: idx for idx, page in enumerate(update)}
        for x, successors in graph.items():
            for y in successors:
                if (
                    x in position
                    and y in position
                    and position[x] > position[y]
                ):
                    return False
        return True

    middle_sum = 0
    for update in updates:
        if is_valid(update):
            middle_sum += update[len(update) // 2]

    return middle_sum


if __name__ == "__main__":
    try:
        result = count_middle_page_number(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
