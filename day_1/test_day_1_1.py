from main_day_1_1 import calculate_total_distance


def test_calculate_total_distance(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """3   4
                    4   3
                    2   5
                    1   3
                    3   9
                    3   3"""
    input_file.write_text(input_data)

    result = calculate_total_distance(str(input_file))
    assert result == 11
