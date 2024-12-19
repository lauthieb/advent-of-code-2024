from main_day_19_2 import sum_all_possible_ways


def test_sum_all_possible_ways(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """r, wr, b, g, bwu, rb, gb, br

                    brwrr
                    bggr
                    gbbr
                    rrbgbr
                    ubwu
                    bwurrg
                    brgr
                    bbrgwb"""
    input_file.write_text(input_data)

    result = sum_all_possible_ways(str(input_file))
    print(result)
    assert result == 16
