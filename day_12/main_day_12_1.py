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


@measure_time
def calculate_total_fencing_cost(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]

    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    DIRECTION_OFFSETS = [
        (-1, 0),  # UP
        (1, 0),   # DOWN
        (0, -1),  # LEFT
        (0, 1)    # RIGHT
    ]

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        region_type = grid[start_row][start_col]
        area = 0
        perimeter = 0

        while queue:
            row, col = queue.popleft()
            if visited[row][col]:
                continue

            visited[row][col] = True
            area += 1

            for row_offset, col_offset in DIRECTION_OFFSETS:
                neighbor_row, neighbor_col = row + row_offset, col + col_offset

                if (
                    0 <= neighbor_row < num_rows
                    and 0 <= neighbor_col < num_cols
                ):
                    if grid[neighbor_row][neighbor_col] == region_type:
                        if not visited[neighbor_row][neighbor_col]:
                            queue.append((neighbor_row, neighbor_col))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    total_cost = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if not visited[row][col]:
                area, perimeter = bfs(row, col)
                total_cost += area * perimeter

    return total_cost


if __name__ == "__main__":
    try:
        result = calculate_total_fencing_cost(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
