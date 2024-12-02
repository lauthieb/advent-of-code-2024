def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def calculate_safe_count(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    safe_count = 0
    for line in lines:
        if is_safe(line.strip()):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    result = calculate_safe_count("input.txt")
    print(result)
