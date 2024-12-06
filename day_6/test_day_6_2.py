from main_day_6_2 import count_possible_obstacle_positions


def test_count_possible_obstacle_positions(tmp_path):
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

    result = count_possible_obstacle_positions(str(input_file))
    print(result)
    assert result == 6
