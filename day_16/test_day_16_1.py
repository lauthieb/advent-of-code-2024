from main_day_16_1 import calculate_lowest_score


def test_calculate_lowest_score(tmp_path):
    input_file_1 = tmp_path / "input.txt"
    input_data_1 = """###############
                      #.......#....E#
                      #.#.###.#.###.#
                      #.....#.#...#.#
                      #.###.#####.#.#
                      #.#.#.......#.#
                      #.#.#####.###.#
                      #...........#.#
                      ###.#.#####.#.#
                      #...#.....#.#.#
                      #.#.#.###.#.#.#
                      #.....#...#.#.#
                      #.###.#.#.#.#.#
                      #S..#.....#...#
                      ###############"""
    input_file_1.write_text(input_data_1)

    result_1 = calculate_lowest_score(str(input_file_1))
    print(result_1)
    assert result_1 == 7036

    input_file_2 = tmp_path / "input.txt"
    input_data_2 = """#################
                      #...#...#...#..E#
                      #.#.#.#.#.#.#.#.#
                      #.#.#.#...#...#.#
                      #.#.#.#.###.#.#.#
                      #...#.#.#.....#.#
                      #.#.#.#.#.#####.#
                      #.#...#.#.#.....#
                      #.#.#####.#.###.#
                      #.#.#.......#...#
                      #.#.###.#####.###
                      #.#.#...#.....#.#
                      #.#.#.#####.###.#
                      #.#.#.........#.#
                      #.#.#.#########.#
                      #S#.............#
                      #################"""
    input_file_2.write_text(input_data_2)

    result_2 = calculate_lowest_score(str(input_file_2))
    print(result_2)
    assert result_2 == 11048
