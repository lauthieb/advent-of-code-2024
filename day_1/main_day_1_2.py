def calculate_similarity_score(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    array1 = []
    array2 = []

    for i in range(len(lines)):
        inputs = " ".join(lines[i].strip().split()).split(" ")
        array1.append(inputs[0])
        array2.append(inputs[1])

    array1 = [int(numeric_string) for numeric_string in array1]
    array2 = [int(numeric_string) for numeric_string in array2]

    similarity_score = 0
    for i in range(len(array1)):
        similarity_score += array1[i] * array2.count(array1[i])

    return similarity_score


if __name__ == "__main__":
    result = calculate_similarity_score("input.txt")
    print(result)
