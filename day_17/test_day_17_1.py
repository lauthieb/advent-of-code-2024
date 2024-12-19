from main_day_17_1 import run_chronospatial_computer


def test_run_chronospatial_computer(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """Register A: 729
                    Register B: 0
                    Register C: 0

                    Program: 0,1,5,4,3,0"""
    input_file.write_text(input_data)

    result = run_chronospatial_computer(str(input_file))
    print(result)
    assert result == "4,6,3,5,6,3,5,2,1,0"
