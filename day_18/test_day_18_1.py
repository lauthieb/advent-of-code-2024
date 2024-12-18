from main_day_18_1 import calculate_minimum_steps


def test_calculate_minimum_steps(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """5,4
                    4,2
                    4,5
                    3,0
                    2,1
                    6,3
                    2,4
                    1,5
                    0,6
                    3,3
                    2,6
                    5,1
                    1,2
                    5,5
                    2,5
                    6,5
                    1,4
                    0,4
                    6,4
                    1,1
                    6,1
                    1,0
                    0,5
                    1,6
                    2,0"""
    input_file.write_text(input_data)

    result = calculate_minimum_steps(
        str(input_file),
        grid_size=7,
        corrupted_length=12
    )
    print(result)
    assert result == 22
