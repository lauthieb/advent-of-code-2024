import sys
import os
import heapq  # Importation du module heapq

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


# TODO: should be optimized... ~100 seconds 😬⏳
@measure_time
def calculate_tiles(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]
        num_rows, num_cols = len(grid), len(grid[0])
        start_pos = None
        end_pos = None
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "S":
                    start_pos = (r, c)
                elif grid[r][c] == "E":
                    end_pos = (r, c)
            if start_pos and end_pos:
                break

        paths = []
        visited = {}

        queue = []  # (score, position, direction, history)
        heapq.heappush(
            queue,
            (0, start_pos, 0, [start_pos])
        )

        while queue:
            curr_score, (r, c), curr_dir, history = heapq.heappop(queue)

            if (r, c) == end_pos:
                paths.append((history, curr_score))
                continue

            if (
                ((r, c), curr_dir) in visited
                and visited[((r, c), curr_dir)] < curr_score
            ):
                continue

            visited[((r, c), curr_dir)] = curr_score

            for _dir, (dr, dc) in enumerate(DIRECTIONS):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] != "#"
                    and (nr, nc) not in history
                ):
                    if _dir == curr_dir:
                        heapq.heappush(queue, (
                            curr_score + 1,
                            (nr, nc),
                            _dir,
                            history + [(nr, nc)]
                        ))
                    else:
                        heapq.heappush(queue, (
                            curr_score + 1000,
                            (r, c),
                            _dir,
                            history
                        ))

        min_score = min(r[1] for r in paths)
        best_paths = [r for r in paths if r[1] == min_score]
        tiles = {tile for path in best_paths for tile in path[0]}
        return len(tiles)


if __name__ == "__main__":
    try:
        result = calculate_tiles(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
