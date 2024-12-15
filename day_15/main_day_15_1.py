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

DIRECTION_OFFSETS = {
    "^": (-1, 0),  # Up
    ">": (0, 1),   # Right
    "v": (1, 0),   # Down
    "<": (0, -1),  # Left
}


def can_move(grid, r, c, dr, dc):
    new_r, new_c = r + dr, c + dc
    return (
        0 <= new_r < len(grid)
        and 0 <= new_c < len(grid[0])
        and grid[new_r][new_c] != '#'
    )


def push_boxes(grid, r, c, dr, dc):
    new_r, new_c = r + dr, c + dc
    boxes_to_move = []

    while 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
        if grid[new_r][new_c] == 'O':
            if not can_move(grid, new_r, new_c, dr, dc):
                return False
            boxes_to_move.append((new_r, new_c))
        elif grid[new_r][new_c] in {'#', '.'}:
            break
        new_r += dr
        new_c += dc

    for box_r, box_c in reversed(boxes_to_move):
        grid[box_r][box_c] = '.'
        grid[box_r + dr][box_c + dc] = 'O'

    return True


def find_robot(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '@':
                return r, c

    raise ValueError("Robot not found in the grid.")


def simulate_robot_moves(grid, moves):
    robot_r, robot_c = find_robot(grid)

    for move in moves:
        dr, dc = DIRECTION_OFFSETS[move]
        new_r, new_c = robot_r + dr, robot_c + dc

        if can_move(grid, robot_r, robot_c, dr, dc):
            if (
                grid[new_r][new_c] == 'O'
                and not push_boxes(grid, robot_r, robot_c, dr, dc)
            ):
                continue

            grid[robot_r][robot_c] = '.'
            robot_r, robot_c = new_r, new_c
            grid[robot_r][robot_c] = '@'

    return grid


@measure_time
def calculate_boxes_coordinates(input_file):
    with open(input_file, "r") as f:
        grid_str, moves = f.read().split("\n\n")
        grid = [list(row.strip()) for row in grid_str.split("\n")]
        moves = moves.replace("\n", "").replace(" ", "")

    final_grid = simulate_robot_moves(grid, moves)

    return sum(
        r * 100 + c for r, row in enumerate(final_grid)
        for c, val in enumerate(row) if val == 'O'
    )


if __name__ == "__main__":
    try:
        result = calculate_boxes_coordinates(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
