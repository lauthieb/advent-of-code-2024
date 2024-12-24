import sys
import os
import re
from collections import defaultdict, deque

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


def evaluate_gates(initial_values, gates):
    wire_values = initial_values.copy()
    dependencies = defaultdict(list)

    parsed_gates = []
    for gate in gates:
        match = re.match(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", gate)
        if match:
            input1, operation, input2, output = match.groups()
            parsed_gates.append((input1, input2, operation, output))
            dependencies[input1].append(output)
            dependencies[input2].append(output)

    queue = deque(initial_values.keys())
    while queue:
        queue.popleft()

        for gate in parsed_gates:
            input1, input2, operation, output = gate
            if output in wire_values:
                continue
            if input1 in wire_values and input2 in wire_values:
                val1 = wire_values[input1]
                val2 = wire_values[input2]
                if operation == "AND":
                    wire_values[output] = val1 & val2
                elif operation == "OR":
                    wire_values[output] = val1 | val2
                elif operation == "XOR":
                    wire_values[output] = val1 ^ val2
                queue.append(output)

    return wire_values


def calculate_decimal_output(wire_values):
    z_values = sorted(
        (int(wire[1:]), value)
        for wire, value in wire_values.items()
        if wire.startswith("z")
    )
    binary_number = "".join(
        str(value) for _, value in sorted(z_values, reverse=True)
    )
    return int(binary_number, 2)


@measure_time
def simulate_system(input_file, picoseconds=100):
    with open(input_file, "r") as f:
        data = [line.strip() for line in f.readlines()]

    initial_values = {}
    gates = []

    for line in data:
        if ":" in line:
            wire, value = line.split(": ")
            initial_values[wire] = int(value)
        else:
            if line != "":
                gates.append(line)

    wire_values = evaluate_gates(initial_values, gates)

    return calculate_decimal_output(wire_values)


if __name__ == "__main__":
    try:
        result = simulate_system(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
