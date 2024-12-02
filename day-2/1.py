f = open("input.txt", "r")
lines = f.readlines()


def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


safe_count = 0
for i in range(len(lines)):
    if is_safe(lines[i].strip()):
        safe_count += 1

print(safe_count)
