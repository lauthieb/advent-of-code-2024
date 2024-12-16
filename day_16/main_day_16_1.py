import sys
import os
import heapq

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
    (0, 1),  # East
    (-1, 0),  # North
    (0, -1),  # West
    (1, 0),  # South
]


@measure_time
def calculate_lowest_score(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]
        num_rows, num_cols = len(grid), len(grid[0])
        start_pos, end_pos = None, None
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "S":
                    start_pos = (r, c)
                elif grid[r][c] == "E":
                    end_pos = (r, c)
            if start_pos and end_pos:
                break

        queue = [(0, start_pos, 0)]  # (score, position, direction)
        visited = set()

        while queue:
            curr_score, (r, c), curr_dir = heapq.heappop(queue)
            if (r, c) == end_pos:
                return curr_score
            if ((r, c), curr_dir) in visited:
                continue
            visited.add(((r, c), curr_dir))

            for _dir, (dr, dc) in enumerate(DIRECTIONS):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] != "#"
                ):
                    new_score = curr_score + 1
                    if _dir != curr_dir:
                        new_score += 1000
                    heapq.heappush(queue, (new_score, (nr, nc), _dir))

        return -1


if __name__ == "__main__":
    try:
        result = calculate_lowest_score(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
