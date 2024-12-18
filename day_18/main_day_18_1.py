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


@measure_time
def calculate_minimum_steps(input_file, grid_size=71, corrupted_length=1024):
    with open(input_file, "r") as f:
        corrupted = [[*map(int, line.split(","))] for line in f]
        grid = [["."] * grid_size for _ in range(grid_size)]
        for x, y in corrupted[:corrupted_length]:
            grid[y][x] = "#"

        start = (0, 0)
        end = (grid_size - 1, grid_size - 1)
        queue = [(start, 0)]
        seen = set()

        while queue:
            pos, length = queue.pop(0)
            if pos == end:
                return length
            if pos in seen:
                continue
            seen.add(pos)
            x, y = pos
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < grid_size
                    and 0 <= ny < grid_size
                    and grid[ny][nx] == "."
                ):
                    queue.append(((nx, ny), length + 1))


if __name__ == "__main__":
    try:
        result = calculate_minimum_steps(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
