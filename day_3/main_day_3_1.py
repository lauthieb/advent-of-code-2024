import re


def get_multiply(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    total_sum = 0

    for line in lines:
        matches = re.findall(pattern, line)

        for match in matches:
            numbers = re.search(r"\((\d{1,3}),(\d{1,3})\)", match)
            if numbers:
                a, b = int(numbers.group(1)), int(numbers.group(2))
                total_sum += a * b

    return total_sum


if __name__ == "__main__":
    result = get_multiply("input.txt")
    print(result)
