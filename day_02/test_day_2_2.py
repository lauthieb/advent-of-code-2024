from main_day_2_2 import calculate_safe_count


def test_calculate_safe_count(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """7 6 4 2 1
                    1 2 7 8 9
                    9 7 6 2 1
                    1 3 2 4 5
                    8 6 4 4 1
                    1 3 6 7 9"""
    input_file.write_text(input_data)

    result = calculate_safe_count(str(input_file))
    assert result == 4
