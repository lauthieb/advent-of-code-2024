from main_day_7_2 import count_total_calibration


def test_count_total_calibration(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """190: 10 19
                    3267: 81 40 27
                    83: 17 5
                    156: 15 6
                    7290: 6 8 6 15
                    161011: 16 10 13
                    192: 17 8 14
                    21037: 9 7 18 13
                    292: 11 6 16 20"""
    input_file.write_text(input_data)

    result = count_total_calibration(str(input_file))
    print(result)
    assert result == 11387
