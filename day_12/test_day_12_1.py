from main_day_12_1 import calculate_total_fencing_cost


def test_calculate_total_fencing_cost(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """RRRRIICCFF
                    RRRRIICCCF
                    VVRRRCCFFF
                    VVRCCCJFFF
                    VVVVCJJCFE
                    VVIVCCJJEE
                    VVIIICJJEE
                    MIIIIIJJEE
                    MIIISIJEEE
                    MMMISSJEEE"""
    input_file.write_text(input_data)

    result = calculate_total_fencing_cost(str(input_file))
    print(result)
    assert result == 1930
