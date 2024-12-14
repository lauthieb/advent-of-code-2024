from main_day_14_1 import calculate_safety_factor


def test_calculate_safety_factor(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """p=0,4 v=3,-3
                    p=6,3 v=-1,-3
                    p=10,3 v=-1,2
                    p=2,0 v=2,-1
                    p=0,0 v=1,3
                    p=3,0 v=-2,-2
                    p=7,6 v=-1,-3
                    p=3,0 v=-1,-2
                    p=9,3 v=2,3
                    p=7,3 v=-1,2
                    p=2,4 v=2,-3
                    p=9,5 v=-3,-3"""
    input_file.write_text(input_data)

    result = calculate_safety_factor(str(input_file), 11, 7)
    print(result)
    assert result == 12
