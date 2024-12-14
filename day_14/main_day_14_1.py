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
def calculate_safety_factor(input_file, grid_width=101, grid_height=103):
    with open(input_file, "r") as f:
        robots = []
        for line in f:
            position, velocity = line.strip().split(" v=")
            px, py = map(int, position[2:].split(","))
            vx, vy = map(int, velocity.split(","))
            robots.append(((px, py), (vx, vy)))

        times = 100

        def wrap_position(x, y):
            return x % grid_width, y % grid_height

        for i in range(len(robots)):
            (px, py), (vx, vy) = robots[i]
            px, py = wrap_position(px + vx * times, py + vy * times)
            robots[i] = ((px, py), (vx, vy))

        grid = [[0] * grid_width for _ in range(grid_height)]
        for (px, py), _ in robots:
            grid[py][px] += 1

        mid_x, mid_y = grid_width // 2, grid_height // 2
        quadrants = [0, 0, 0, 0]

        for y in range(grid_height):
            for x in range(grid_width):
                if x == mid_x or y == mid_y:
                    continue
                if x < mid_x and y < mid_y:
                    quadrants[0] += grid[y][x]
                elif x >= mid_x and y < mid_y:
                    quadrants[1] += grid[y][x]
                elif x < mid_x and y >= mid_y:
                    quadrants[2] += grid[y][x]
                elif x >= mid_x and y >= mid_y:
                    quadrants[3] += grid[y][x]

        safety_factor = 1
        for count in quadrants:
            safety_factor *= count

        return safety_factor


if __name__ == "__main__":
    try:
        result = calculate_safety_factor(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
