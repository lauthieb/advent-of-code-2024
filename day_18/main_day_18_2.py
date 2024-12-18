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

DIRECTIONS = [
    (-1, 0),  # Top
    (0, 1),  # Right
    (1, 0),  # Bottom
    (0, -1),  # Left
]


def is_path_possible(grid, grid_size):
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    queue = [start]
    seen = set()

    while queue:
        pos = queue.pop(0)
        if pos == end:
            return True
        if pos in seen:
            continue
        seen.add(pos)
        row, col = pos
        for dx, dy in DIRECTIONS:
            nx, ny = row + dx, col + dy
            if (
                0 <= nx < grid_size
                and 0 <= ny < grid_size
                and grid[ny][nx] == "."
            ):
                queue.append((nx, ny))
    return False


@measure_time
def find_first_blocking_byte(input_file, grid_size=71):
    with open(input_file, "r") as f:
        corrupted = [[*map(int, line.split(","))] for line in f]

    low = 0
    high = len(corrupted) - 1
    blocking_byte_index = -1

    # Binary search
    while low <= high:
        mid = (low + high) // 2
        grid = [["."] * grid_size for _ in range(grid_size)]
        for row, col in corrupted[:mid + 1]:
            grid[row][col] = "#"

        if is_path_possible(grid, grid_size):
            low = mid + 1  # Path still exists, check further
        else:
            blocking_byte_index = mid
            high = mid - 1  # Path blocked, check earlier

    if blocking_byte_index != -1:
        return ",".join(str(x) for x in corrupted[blocking_byte_index])


if __name__ == "__main__":
    try:
        result = find_first_blocking_byte(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
