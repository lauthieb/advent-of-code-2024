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


@measure_time
def calculate_filesystem_checksum(input_file):
    with open(input_file, "r") as f:
        line = [line for line in f][0]
        is_file = True
        files = []
        free_spaces = [[] for i in range(10)]
        position, file_id = 0, 0
        for digit in line:
            digit = int(digit)
            if is_file:
                files.append([position, file_id, digit])
                file_id += 1
            else:
                heapq.heappush(free_spaces[digit], position)
            position += digit
            is_file = not is_file

        checksum = 0
        for f in range(len(files))[::-1]:
            file_position, file_id, file_size = files[f]

            best_position = file_position
            free_space_candidates = [
                (heapq.heappop(free_spaces[i]), i)
                for i in range(10)
                if free_spaces[i] and i >= file_size
            ]
            if free_space_candidates:
                available_position, max_free_space = min(free_space_candidates)
                if available_position < file_position:
                    best_position = available_position
                    free_space_candidates.remove(
                        (available_position, max_free_space)
                    )
                    heapq.heappush(
                        free_spaces[max_free_space-file_size],
                        available_position + file_size
                    )
                for available_position, max_free_space in \
                        free_space_candidates:
                    heapq.heappush(
                        free_spaces[max_free_space],
                        available_position
                    )
                files[f][0] = best_position

            start = best_position
            end = best_position + file_size - 1
            position_sum = (start + end) * file_size // 2
            checksum += file_id * position_sum
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
