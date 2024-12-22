from main_day_22_2 import get_most_bananas


def test_get_most_bananas(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """1
                    2
                    3
                    2024"""
    input_file.write_text(input_data)

    result = get_most_bananas(str(input_file))
    print(result)
    assert result == 23
