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
def calculate_lock_key_pairs_without_overlapping(input_file):
    with open(input_file, "r") as f:
        content = f.read()
        grids = [
            [list(line.strip()) for line in block.splitlines() if line.strip()]
            for block in content.strip().split("\n\n")
        ]

        locks = [
            grid for grid in grids
            if all(cell == "#" for cell in grid[0])
            and all(cell == "." for cell in grid[len(grid) - 1])
        ]
        locks_heights = [
            [column.count('#') - 1 for column in zip(*lock)]
            for lock in locks
        ]
        keys = [
            grid for grid in grids
            if all(cell == "." for cell in grid[0])
            and all(cell == "#" for cell in grid[len(grid) - 1])
        ]
        keys_heights = [
            [column.count('#') - 1 for column in zip(*key)]
            for key in keys
        ]

        key_pairs_without_overlapping = [
            (lock_row, key_row)
            for lock_row in locks_heights
            for key_row in keys_heights
            if all(lock + key <= 5 for lock, key in zip(lock_row, key_row))
        ]

    return len(key_pairs_without_overlapping)


if __name__ == "__main__":
    try:
        result = calculate_lock_key_pairs_without_overlapping(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
