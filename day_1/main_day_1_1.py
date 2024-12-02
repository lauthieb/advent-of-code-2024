def calculate_total_distance(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    array1 = []
    array2 = []

    for i in range(len(lines)):
        inputs = " ".join(lines[i].strip().split()).split(" ")
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
    result = calculate_total_distance("input.txt")
    print(result)
