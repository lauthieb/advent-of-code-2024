import sys
import os
from collections import deque

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


def calculate_area(region: set[tuple[int, int]]) -> int:
    return len(region)


def parse_regions(grid: list[str]) -> list[set[tuple[int, int]]]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    regions = []
    seen = set()

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in seen:
                continue
            region = set()
            queue = deque([(r, c)])
            while queue:
                rr, cc = queue.popleft()
                region.add((rr, cc))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = rr + dr, cc + dc
                    if (
                        (nr, nc) not in seen and
                        0 <= nr < num_rows and
                        0 <= nc < num_cols and
                        grid[nr][nc] == grid[rr][cc]
                    ):
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            regions.append(region)
    return regions


@measure_time
def calculate_total_fencing_cost(input_file: str):
    with open(input_file, "r") as f:
        grid = list(map(str.strip, f.readlines()))

    regions = parse_regions(grid)

    return sum(calculate_area(r) * calculate_sides(r) for r in regions)


def calculate_sides(region: set[tuple[int, int]]) -> int:
    up, down, left, right = (set() for _ in range(4))
    for r, c in region:
        if (r - 1, c) not in region:
            up.add((r, c))
        if (r + 1, c) not in region:
            down.add((r, c))
        if (r, c - 1) not in region:
            left.add((r, c))
        if (r, c + 1) not in region:
            right.add((r, c))

    count = 0
    for (r, c) in up:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            count += 1

    for (r, c) in down:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            count += 1

    return count


if __name__ == "__main__":
    try:
        result = calculate_total_fencing_cost(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
