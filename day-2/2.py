f = open("input.txt", "r")
lines = f.readlines()


def generate_subsets(report):
    return [
        report[:i]
        + report[i + 1:]
        for i in range(len(report))
    ]


def is_safe(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


safe_count = 0
for i in range(len(lines)):

    if is_safe(list(map(int, lines[i].strip().split()))):
        safe_count += 1
    else:
        for subset in generate_subsets(list(map(int,
                                                lines[i].strip().split()))):
            if is_safe(subset):
                safe_count += 1
                break

print(safe_count)
