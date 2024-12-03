import re


def get_multiply(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    total_sum = 0
    operations = []

    for line in lines:
        matches = re.findall(pattern, line)
        operations.extend(matches)

    should_take_mul = True

    for operation in operations:
        if operation.startswith("mul") and should_take_mul:
            numbers = re.search(r"\((\d{1,3}),(\d{1,3})\)", operation)
            if numbers:
                a, b = int(numbers.group(1)), int(numbers.group(2))
                total_sum += a * b
        elif operation == "don't()":
            should_take_mul = False
        elif operation == "do()":
            should_take_mul = True

    return total_sum


if __name__ == "__main__":
    result = get_multiply("input.txt")
    print(result)
