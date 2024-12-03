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
def calculate_total_distance(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    array1 = []
    array2 = []

    for i in range(len(lines)):
        inputs = lines[i].strip().split()
        array1.append(inputs[0])
        array2.append(inputs[1])

    array1 = [int(numeric_string) for numeric_string in array1]
    array1.sort()
    array2 = [int(numeric_string) for numeric_string in array2]
    array2.sort()

    total_distance = 0

    for i in range(len(array1)):
        total_distance += abs(array1[i] - array2[i])

    return total_distance


if __name__ == "__main__":
    try:
        result = calculate_total_distance(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
