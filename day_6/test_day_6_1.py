from main_day_6_1 import count_distinct_positions


def test_count_distinct_positions(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """....#.....
                    .........#
                    ..........
                    ..#.......
                    .......#..
                    ..........
                    .#..^.....
                    ........#.
                    #.........
                    ......#..."""
    input_file.write_text(input_data)

    result = count_distinct_positions(str(input_file))
    print(result)
    assert result == 41
