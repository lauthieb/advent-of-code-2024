from main_day_13_2 import find_minimum_tokens


def test_find_minimum_tokens(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """Button A: X+94, Y+34
                    Button B: X+22, Y+67
                    Prize: X=8400, Y=5400

                    Button A: X+26, Y+66
                    Button B: X+67, Y+21
                    Prize: X=12748, Y=12176

                    Button A: X+17, Y+86
                    Button B: X+84, Y+37
                    Prize: X=7870, Y=6450

                    Button A: X+69, Y+23
                    Button B: X+27, Y+71
                    Prize: X=18641, Y=10279"""
    input_file.write_text(input_data)

    result = find_minimum_tokens(str(input_file))
    print(result)
    assert result == 875318608908
