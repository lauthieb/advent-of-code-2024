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
def find_minimum_tokens(input_file):
    with open(input_file, "r") as f:
        lines = f.read().strip().split("\n\n")

    min_tokens = 0

    for machine in lines:
        button_a, button_b, prize = machine.split("\n")
        button_a = list(map(
            int,
            [button_a.split("X+")[1].split(",")[0], button_a.split("Y+")[1]]
        ))
        button_b = list(map(
            int,
            [button_b.split("X+")[1].split(",")[0], button_b.split("Y+")[1]]
        ))
        prize = list(map(
            lambda num: int(num) + 10000000000000,
            [
                prize.split("X=")[1].split(",")[0],
                prize.split("Y=")[1]]
        ))

        button_b_presses = (prize[1] * button_a[0] - prize[0] * button_a[1]) \
            / (button_b[1] * button_a[0] - button_b[0] * button_a[1])
        button_a_presses = (prize[0] - button_b[0] * button_b_presses) \
            / button_a[0]

        if (
            button_a_presses.is_integer()
            and button_b_presses.is_integer()
        ):
            min_tokens += int(button_a_presses) * 3 + int(button_b_presses)

    return min_tokens


if __name__ == "__main__":
    try:
        result = find_minimum_tokens(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
