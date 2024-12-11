from main_day_11_2 import calculate_number_of_stones


def test_calculate_number_of_stones(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = "125 17"
    input_file.write_text(input_data)

    result = calculate_number_of_stones(str(input_file))
    print(result)
    assert result == 55312
