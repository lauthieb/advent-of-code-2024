import sys
import os
from itertools import combinations

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


def find_triads(connections):
    triads = set()
    for node in connections:
        neighbors = connections[node]
        for a, b in combinations(neighbors, 2):
            if b in connections[a]:
                triad = tuple(sorted([node, a, b]))
                triads.add(triad)
    return triads


@measure_time
def calculate_triads_with_t(input_file):
    with open(input_file, "r") as f:
        connections = {}
        for line in f:
            a, b = line.strip().split("-")
            connections.setdefault(a, set()).add(b)
            connections.setdefault(b, set()).add(a)

        triads = find_triads(connections)
        filtered_triads = [
            triad for triad in triads
            if any(node.startswith("t") for node in triad)
        ]
        return len(filtered_triads)


if __name__ == "__main__":
    try:
        result = calculate_triads_with_t(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
