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
def calculate_number_of_stones(input_file):
    with open(input_file, "r") as f:
        line = [line for line in f][0]
        stones = [int(n) for n in line.split()]

        blink = 0

        while blink < 25:
            next_stones = []
            for i in range(len(stones)):
                if (stones[i] == 0):
                    next_stones.append(1)
                elif (len(str(stones[i])) % 2 == 0):
                    current_stone = str(stones[i])
                    midpoint = len(current_stone) // 2
                    first_stone = current_stone[:midpoint].lstrip("0")
                    if (first_stone == ""):
                        first_stone = "0"
                    second_stone = current_stone[midpoint:].lstrip("0")
                    if (second_stone == ""):
                        second_stone = "0"
                    next_stones.extend([int(first_stone), int(second_stone)])
                else:
                    next_stones.append(stones[i] * 2024)
            stones = next_stones
            blink += 1

        return len(stones)


if __name__ == "__main__":
    try:
        result = calculate_number_of_stones(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
