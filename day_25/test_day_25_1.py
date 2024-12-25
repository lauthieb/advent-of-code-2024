from main_day_25_1 import calculate_lock_key_pairs_without_overlapping


def test_calculate_lock_key_pairs_without_overlapping(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """#####
                    .####
                    .####
                    .####
                    .#.#.
                    .#...
                    .....

                    #####
                    ##.##
                    .#.##
                    ...##
                    ...#.
                    ...#.
                    .....

                    .....
                    #....
                    #....
                    #...#
                    #.#.#
                    #.###
                    #####

                    .....
                    .....
                    #.#..
                    ###..
                    ###.#
                    ###.#
                    #####

                    .....
                    .....
                    .....
                    #....
                    #.#..
                    #.#.#
                    #####"""
    input_file.write_text(input_data)

    result = calculate_lock_key_pairs_without_overlapping(str(input_file))
    print(result)
    assert result == 3
