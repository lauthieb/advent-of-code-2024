import sys
import os
from collections import deque

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
def calculate_filesystem_checksum(input_file):
    with open(input_file, "r") as f:
        line = [line for line in f][0]
        blocks = deque(enumerate(int(n) for n in line[::2]))
        free_spaces = deque(int(n) for n in line[1::2])

        compacted = []
        while blocks:
            front_block = blocks.popleft()
            compacted.append(front_block)
            if free_spaces:
                front_gap = free_spaces.popleft()
                while blocks and front_gap:
                    block_id, block_size = blocks.pop()
                    if block_size <= front_gap:
                        compacted.append((block_id, block_size))
                        front_gap -= block_size
                    else:
                        compacted.append((block_id, front_gap))
                        blocks.append((block_id, block_size - front_gap))
                        front_gap = 0

        checksum = 0
        position = 0

        for block_id, block_size in compacted:
            for _ in range(block_size):
                checksum += block_id * position
                position += 1

        return checksum


if __name__ == "__main__":
    try:
        result = calculate_filesystem_checksum(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
