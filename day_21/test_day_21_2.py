from main_day_21_2 import calculate_sum_complexities


def test_calculate_sum_complexities(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """029A
                    980A
                    179A
                    456A
                    379A"""
    input_file.write_text(input_data)

    result = calculate_sum_complexities(str(input_file))
    print(result)
    assert result == 154115708116294
