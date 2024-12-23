import sys
import os
import networkx as nx

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


@measure_time
def calculate_lan_party_password(input_file):
    with open(input_file, "r") as f:
        graph = nx.Graph()

        for line in f:
            a, b = line.strip().split("-")
            graph.add_edge(a, b)

        cliques = nx.find_cliques(graph)
        largest_lan = sorted(sorted(cliques, key=len, reverse=True)[0])
        return ",".join(largest_lan)


if __name__ == "__main__":
    try:
        result = calculate_lan_party_password(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    exit(0)
