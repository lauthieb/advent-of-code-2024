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
        num_rows, num_cols = len(grid), len(grid[0])
        score = 0

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    paths = []
                    queue = [(i, j)]
                    while queue:
                        current_row_id, current_col_id = queue.pop(0)
                        current_value = grid[current_row_id][current_col_id]
                        next_value = current_value + 1
                        for row_offset, col_offset in DIRECTION_OFFSETS:
                            next_row_id, next_col_id = \
                                current_row_id + row_offset, \
                                current_col_id + col_offset
                            if (
                                0 <= next_row_id < num_rows and
                                0 <= next_col_id < num_cols and
                                grid[next_row_id][next_col_id] == next_value
                            ):
                                if next_value == 9:
                                    paths.append((next_row_id, next_col_id))
                                else:
                                    queue.append((next_row_id, next_col_id))

                    score += len(paths)
        return score


if __name__ == "__main__":
    try:
        result = calculate_tailheads_score(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
