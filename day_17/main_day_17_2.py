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


def get_operand_value(operand, registers, is_combo=False):
    if not is_combo:
        return operand
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    raise ValueError(f"Not valid operand: {operand}")


def execute_program(program, registers):
    output = []
    instruction_pointer = 0

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv: Divide A by 2^combo_operand
            combo_operand = get_operand_value(
                operand, registers, is_combo=True)
            registers["A"] //= 2 ** combo_operand

        elif opcode == 1:  # bxl: XOR bit to bit between B and literal_operand
            literal_operand = get_operand_value(
                operand, registers, is_combo=False)
            registers["B"] ^= literal_operand

        elif opcode == 2:  # bst: B takes the value combo_operand % 8
            combo_operand = get_operand_value(
                operand, registers, is_combo=True)
            registers["B"] = combo_operand % 8

        elif opcode == 3:  # jnz: Jump if A != 0
            literal_operand = get_operand_value(
                operand, registers, is_combo=False)
            if registers["A"] != 0:
                instruction_pointer = literal_operand
                continue  # Don't increment the pointer

        elif opcode == 4:  # bxc: B takes the XOR bit to bit between B and C
            registers["B"] ^= registers["C"]

        elif opcode == 5:  # out: Output combo_operand % 8
            combo_operand = get_operand_value(
                operand, registers, is_combo=True)
            output.append(combo_operand % 8)

        elif opcode == 6:  # bdv: Division like adv but result inside B
            combo_operand = get_operand_value(
                operand, registers, is_combo=True)
            registers["B"] = registers["A"] >> combo_operand
            # same as, registers["B"] = registers["A"] // (2 ** combo_operand)

        elif opcode == 7:  # cdv: Division like adv but result inside C
            combo_operand = get_operand_value(
                operand, registers, is_combo=True)
            registers["C"] = registers["A"] >> combo_operand
            # same as, registers["C"] = registers["A"] // (2 ** combo_operand)

        else:
            raise ValueError(f"Opcode not supported: {opcode}")

        instruction_pointer += 2

    return output


@measure_time
def run_chronospatial_computer(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    registers = {}
    program = []

    for line in lines:
        line = line.lstrip()
        if line.startswith("Program"):
            program = list(map(int, line.split(":")[1].strip().split(",")))

    registers["A"] = sum(7 * 8**i for i in range(len(program) - 1)) + 1
    registers["B"] = 0
    registers["C"] = 0

    while True:
        result = execute_program(program, registers.copy())

        if len(result) > len(program):
            raise ValueError("The output is too long")

        if result == program:
            return registers["A"]

        add = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                add = 8**i
                registers["A"] += add
                break


if __name__ == "__main__":
    try:
        result = run_chronospatial_computer(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
