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
def get_most_bananas(input_file):
    with open(input_file, "r") as f:
        lines = list(map(int, f.readlines()))
        prices = []

        for line in lines:
            price = []
            for _ in range(2000):
                line = ((line * 64) ^ line) % 16777216
                line = ((line // 32) ^ line) % 16777216
                line = ((line * 2048) ^ line) % 16777216
                price.append(line % 10)  # get the last digit
            prices.append(price)

        differences = [[b - a for a, b in zip(p, p[1:])] for p in prices]

        amounts = defaultdict(int)
        for index, diff in enumerate(differences):
            seen = set()
            for i in range(len(diff) - 3):
                key = tuple(diff[i:i + 4])
                if key in seen:
                    continue
                amounts[key] += prices[index][i + 4]
                seen.add(key)

        return max(amounts.values())


if __name__ == "__main__":
    try:
        result = get_most_bananas(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
