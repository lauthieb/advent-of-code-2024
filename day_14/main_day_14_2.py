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

        t = 0

        while True:
            t += 1
            pos = set()
            valid = True

            for (x, y), (vx, vy) in robots:
                x = (x + t * (vx + grid_width)) % grid_width
                y = (y + t * (vy + grid_height)) % grid_height
                if (x, y) in pos:
                    valid = False
                    break
                pos.add((x, y))

            if valid:
                return t


if __name__ == "__main__":
    try:
        result = calculate_safety_factor(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
