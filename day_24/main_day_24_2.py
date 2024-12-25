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
def find_correct_swaps(input_file):
    def parse_file(file):
        wires, operations, highest_z = {}, [], "z00"
        for line in file:
            if ":" in line:
                wire, value = line.strip().split(": ")
                wires[wire] = int(value)
            elif "->" in line:
                op1, op, op2, _, res = line.strip().split(" ")
                operations.append((op1, op, op2, res))
                if res.startswith("z") and int(res[1:]) > int(highest_z[1:]):
                    highest_z = res
        return wires, operations, highest_z

    def identify_wrong_operations(operations, highest_z):
        wrong = set()
        for op1, op, op2, res in operations:
            if res.startswith("z") and op != "XOR" and res != highest_z:
                wrong.add(res)
            if op == "XOR" and all(x[0] not in "xyz" for x in (res, op1, op2)):
                wrong.add(res)
            if op == "AND" and "x00" not in [op1, op2]:
                wrong.update(
                    res
                    for subop1, subop, subop2, _ in operations
                    if (res in [subop1, subop2] and subop != "OR")
                )
            if op == "XOR":
                wrong.update(
                    res
                    for subop1, subop, subop2, _ in operations
                    if (res in [subop1, subop2] and subop == "OR")
                )
        return wrong

    def execute_operations(wires, operations):
        while operations:
            op1, op, op2, res = operations.pop(0)
            if op1 in wires and op2 in wires:
                wires[res] = {
                    "AND": wires[op1] & wires[op2],
                    "OR": wires[op1] | wires[op2],
                    "XOR": wires[op1] ^ wires[op2],
                }[op]
            else:
                operations.append((op1, op, op2, res))

    with open(input_file, "r") as f:
        wires, operations, highest_z = parse_file(f.read().splitlines())
        wrong = identify_wrong_operations(operations, highest_z)
        execute_operations(wires, operations)

        bits = "".join(
            str(wires[wire])
            for wire in sorted(wires, reverse=True)
            if wire.startswith("z")
        )
        print(int(bits, 2))
        print(",".join(sorted(wrong)))

        return ",".join(sorted(wrong))


if __name__ == "__main__":
    try:
        print(find_correct_swaps(INPUT_FILE))
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
