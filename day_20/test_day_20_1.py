from main_day_20_1 import calculate_cheats


def test_calculate_cheats(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """###############
                    #...#...#.....#
                    #.#.#.#.#.###.#
                    #S#...#.#.#...#
                    #######.#.#.###
                    #######.#.#...#
                    #######.#.###.#
                    ###..E#...#...#
                    ###.#######.###
                    #...###...#...#
                    #.#####.#.###.#
                    #.#...#.#.#...#
                    #.#.#.#.#.#.###
                    #...#...#...###
                    ###############"""
    input_file.write_text(input_data)

    result = calculate_cheats(str(input_file), picoseconds=1)
    print(result)
    assert result == 44
