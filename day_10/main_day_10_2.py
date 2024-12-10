import sys
import os
from collections import deque
import pprint

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
def calculate_tailheads_score(input_file):
    with open(input_file, "r") as f:
        DIRECTION_OFFSETS = [
            (-1, 0),  # UP
            (0, 1),  # RIGHT
            (1, 0),  # DOWN
            (0, -1)  # LEFT
        ]
        grid = [list(map(int, line.strip())) for line in f]

        num_rows = len(grid)
        num_cols = len(grid[0])
        tailheads_score = 0

        def in_bounds(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        def count_distinct_trails(start_row, start_col):
            queue = deque([(start_row, start_col, [(start_row, start_col)])])
            distinct_trails = set()

            while queue:
                row, col, path = queue.popleft()

                if grid[row][col] == 9:
                    distinct_trails.add(tuple(path))
                    continue

                for row_offset, col_offset in DIRECTION_OFFSETS:
                    next_row, next_col = row + row_offset, col + col_offset
                    if (
                        in_bounds(next_row, next_col)
                        and (next_row, next_col) not in path
                        and grid[next_row][next_col] == grid[row][col] + 1
                    ):
                        queue.append(
                            (next_row, next_col, path + [(next_row, next_col)])
                        )
                        pprint.pp(queue)

            return len(distinct_trails)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 0:
                    tailheads_score += count_distinct_trails(row, col)

        return tailheads_score


if __name__ == "__main__":
    try:
        result = calculate_tailheads_score(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
