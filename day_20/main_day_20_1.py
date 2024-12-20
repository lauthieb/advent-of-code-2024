import sys
import os
from collections import deque, defaultdict

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


def parse_grid(input_file):
    with open(input_file, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    return grid


def find_start(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "S":
                return r, c
    raise ValueError("'S' position not found.")


def calculate_distances(grid, start):
    num_rows, num_cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    distances = {}

    while queue:
        r, c, d = queue.popleft()
        if (r, c) in distances:
            continue
        distances[(r, c)] = d
        for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
            if (
                0 <= nr < num_rows
                and 0 <= nc < num_cols
                and grid[nr][nc] != "#"
                and (nr, nc) not in distances
            ):
                queue.append((nr, nc, d + 1))
    return distances


@measure_time
def calculate_cheats(input_file, picoseconds=100):
    grid = parse_grid(input_file)
    start = find_start(grid)
    distances = calculate_distances(grid, start)
    disable_collision_picoseconds = 2

    num_rows, num_cols = len(grid), len(grid[0])

    shortcuts = defaultdict(int)
    for r, c in distances:
        for len_cheat in range(2, disable_collision_picoseconds + 1):
            for dr in range(len_cheat + 1):
                dc = len_cheat - dr
                for r2, c2 in set([
                    (r + dr, c + dc),
                    (r + dr, c - dc),
                    (r - dr, c + dc),
                    (r - dr, c - dc),
                ]):
                    if (
                        0 <= r2 < num_rows
                        and 0 <= c2 < num_cols
                        and (r2, c2) in distances
                    ):
                        time_saved = \
                            distances[(r2, c2)] - distances[(r, c)] - len_cheat
                        if time_saved >= picoseconds:
                            shortcuts[time_saved] += 1

    return sum(shortcuts.values())


if __name__ == "__main__":
    try:
        result = calculate_cheats(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
