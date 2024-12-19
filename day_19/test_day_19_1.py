from main_day_19_1 import count_possible_designs


def test_count_possible_designs(tmp_path):
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

    result = count_possible_designs(str(input_file))
    print(result)
    assert result == 6
