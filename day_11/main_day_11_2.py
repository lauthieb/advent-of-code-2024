import sys
import os
from collections import Counter

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
def calculate_number_of_stones_optimized(input_file):
    with open(input_file, "r") as f:
        line = [line for line in f][0]
        initial_stones = [int(n) for n in line.split()]

    stone_counts = Counter(initial_stones)

    for _ in range(75):
        next_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                next_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                current_stone = str(stone)
                midpoint = len(current_stone) // 2
                left_part = current_stone[:midpoint].lstrip("0") or "0"
                right_part = current_stone[midpoint:].lstrip("0") or "0"
                next_counts[int(left_part)] += count
                next_counts[int(right_part)] += count
            else:
                next_counts[stone * 2024] += count
        stone_counts = next_counts

    return sum(stone_counts.values())


if __name__ == "__main__":
    try:
        result = calculate_number_of_stones_optimized(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
