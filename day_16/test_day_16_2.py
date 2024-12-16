from main_day_16_2 import calculate_tiles


def test_calculate_tiles(tmp_path):
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

    result_1 = calculate_tiles(str(input_file_1))
    print(result_1)
    assert result_1 == 45

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

    result_2 = calculate_tiles(str(input_file_2))
    print(result_2)
    assert result_2 == 64
