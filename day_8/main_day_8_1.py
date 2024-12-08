import sys
import os
from collections import defaultdict

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
def count_antinode_positions(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]
        num_rows, num_cols = len(grid), len(grid[0])

        antennas = defaultdict(list)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != ".":
                    antennas[grid[row][col]].append((row, col))

        antinodes = set()

        for coords in antennas.values():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))

                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = tuple(
                            [a + b * _dir for a, b in zip(coords[_idx], diff)]
                        )
                        if 0 <= pos[0] < num_rows and 0 <= pos[1] < num_cols:
                            antinodes.add(pos)
        return len(antinodes)


if __name__ == "__main__":
    try:
        result = count_antinode_positions(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
