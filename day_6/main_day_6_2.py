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


# TODO: should be optimized... ~37 seconds 😬⏳
@measure_time
def count_possible_obstacle_positions(input_file):
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

        guard_position = None
        guard_direction = None
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] in "^>v<":
                    guard_position = (row, col)
                    guard_direction = grid[row][col]
                    break
            if guard_position:
                break

        def simulate_guard_movement(
                grid,
                start_position,
                start_direction,
                obstacle_position):
            num_rows = len(grid)
            num_cols = len(grid[0])
            current_position = start_position
            current_direction = start_direction
            visited_positions = set()
            visited_positions.add((current_position, current_direction))

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
                    return False

                if (
                    grid[next_position[0]][next_position[1]] == OBSTACLE
                    or next_position == obstacle_position
                ):
                    current_direction = NEXT_DIRECTION[current_direction]
                else:
                    current_position = next_position
                    if (
                        current_position,
                        current_direction
                    ) in visited_positions:
                        return True
                    visited_positions.add(
                        (current_position, current_direction)
                    )

        empty_positions = [
            (row, col) for row in range(num_rows) for col in range(num_cols)
            if grid[row][col] == '.'
        ]

        valid_obstacle_positions = 0
        for row, col in empty_positions:
            if simulate_guard_movement(
                grid,
                guard_position,
                guard_direction,
                (row, col)
            ):
                valid_obstacle_positions += 1

        return valid_obstacle_positions


if __name__ == "__main__":
    try:
        result = count_possible_obstacle_positions(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
