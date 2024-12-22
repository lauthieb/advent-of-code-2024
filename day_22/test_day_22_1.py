from main_day_22_1 import calculate_sum_each_buyer


def test_calculate_sum_each_buyer(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """1
                    10
                    100
                    2024"""
    input_file.write_text(input_data)

    result = calculate_sum_each_buyer(str(input_file))
    print(result)
    assert result == 37327623
