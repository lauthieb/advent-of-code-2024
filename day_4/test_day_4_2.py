from main_day_4_2 import count_xmas


def test_calculate_safe_count(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """MMMSXXMASM
                    MSAMXMSMSA
                    AMXSXMAAMM
                    MSAMASMSMX
                    XMASAMXAMM
                    XXAMMXXAMA
                    SMSMSASXSS
                    SAXAMASAAA
                    MAMMMXMMMM
                    MXMXAXMASX"""
    input_file.write_text(input_data)

    result = count_xmas(str(input_file))
    print(result)
    assert result == 9
