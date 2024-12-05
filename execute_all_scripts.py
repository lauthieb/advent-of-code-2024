import os
import subprocess


def execute_scripts():
    for folder in sorted(os.listdir(".")):
        if folder.startswith("day_") and os.path.isdir(folder):
            day_number = folder.split("_")[1]
            print(f"\n{'═' * 50}")
            print(f"Day {day_number}")
            for file in os.listdir(folder):
                if file.endswith(".py"):
                    script_path = os.path.join(folder, file)
                    try:
                        subprocess.run(["python", script_path], check=True)
                    except Exception as e:
                        print(f"Error with {script_path} : {e}")
    exit(0)


if __name__ == "__main__":
    execute_scripts()
