from main_day_9_2 import calculate_filesystem_checksum


def test_calculate_filesystem_checksum(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = "2333133121414131402"
    input_file.write_text(input_data)

    result = calculate_filesystem_checksum(str(input_file))
    print(result)
    assert result == 2858
