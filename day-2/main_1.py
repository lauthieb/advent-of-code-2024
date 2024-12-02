def is_safe(report):
    """
    Vérifie si une ligne de rapport est 'safe' selon les critères donnés.

    Args:
    report (str): Une ligne contenant des niveaux séparés par des espaces.

    Returns:
    bool: True si la ligne est 'safe', sinon False.
    """
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def calculate_safe_count(input_file):
    """
    Compte le nombre de lignes 'safe' dans un fichier d'entrée.

    Args:
    input_file (str): Chemin vers le fichier d'entrée.

    Returns:
    int: Nombre de lignes 'safe'.
    """
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
