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

GRID_MAP = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}


def find_robot(grid):
    print(grid)
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '@':
                return r, c

    raise ValueError("Robot not found in the grid.")


def simulate_robot_moves(grid, moves):
    robot_r, robot_c = find_robot(grid)

    for move in moves:
        dr, dc = DIRECTION_OFFSETS[move]
        do_move = True
        to_move = [(robot_r, robot_c)]
        i = 0

        while i < len(to_move):
            rr, cc = to_move[i]
            i += 1
            nr, nc = rr + dr, cc + dc
            if (nr, nc) in to_move:
                continue
            if grid[nr][nc] == '#':
                do_move = False
                break
            if grid[nr][nc] == '.':
                continue
            if grid[nr][nc] == '[':
                to_move.extend([(nr, nc), (nr, nc + 1)])
            elif grid[nr][nc] == ']':
                to_move.extend([(nr, nc), (nr, nc - 1)])
            else:
                assert False

        if not do_move:
            continue

        grid_copy = [list(row) for row in grid]

        robot_r, robot_c = robot_r + dr, robot_c + dc

        for rr, cc in to_move:
            grid[rr][cc] = "."
        for rr, cc in to_move:
            grid[rr + dr][cc + dc] = grid_copy[rr][cc]

    return grid


@measure_time
def calculate_boxes_coordinates(input_file):
    with open(input_file, "r") as f:
        grid_str, moves = f.read().split("\n\n")
        grid = []
        for row in grid_str.splitlines():
            new_row = []
            for val in row.strip():
                new_row.extend(GRID_MAP[val])
            grid.append(new_row)
        moves = moves.replace("\n", "").replace(" ", "")

    final_grid = simulate_robot_moves(grid, moves)

    return sum(
        r * 100 + c for r, row in enumerate(final_grid)
        for c, val in enumerate(row) if val == '['
    )


if __name__ == "__main__":
    try:
        result = calculate_boxes_coordinates(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
