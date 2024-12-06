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
def count_distinct_positions(input_file):
    with open(input_file, "r") as f:
        NEXT_DIRECTION = {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^",
        }
        DIRECTION_OFFSETS = {
            "^": (-1, 0),  # Up
            ">": (0, 1),   # Right
            "v": (1, 0),   # Down
            "<": (0, -1),  # Left
        }
        OBSTACLE = "#"

        grid = [list(line.strip()) for line in f]
        num_rows = len(grid)
        num_cols = len(grid[0])

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] in "^>v<":
                    current_position = (row, col)
                    current_direction = grid[row][col]
                    break

        visited_positions = set()
        visited_positions.add(current_position)

        while True:
            offset = DIRECTION_OFFSETS[current_direction]
            next_position = (
                current_position[0] + offset[0],
                current_position[1] + offset[1]
            )

            if not (
                0 <= next_position[0] < num_rows
                and 0 <= next_position[1] < num_cols
            ):
                break

            if grid[next_position[0]][next_position[1]] == OBSTACLE:
                current_direction = NEXT_DIRECTION[current_direction]
            else:
                current_position = next_position
                visited_positions.add(current_position)

        return len(visited_positions)


if __name__ == "__main__":
    try:
        result = count_distinct_positions(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
