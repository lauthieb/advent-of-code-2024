import os


def create_day_structure(day_number):
    day_folder = f"day_{day_number}"
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)

    files = [
        "input.txt",
        f"main_day_{day_number}_1.py",
        f"main_day_{day_number}_2.py",
        f"test_day_{day_number}_1.py",
        f"test_day_{day_number}_2.py",
    ]

    for file_name in files:
        file_path = os.path.join(day_folder, file_name)
        with open(file_path, "w"):
            pass

    print(f"Structure for day {day_number} created with success!")


if __name__ == "__main__":
    day_number = input(
        "Enter the day number: ")

    try:
        day_number = int(day_number)
        create_day_structure(day_number)
    except ValueError:
        print("Please, enter a valid day number.")
