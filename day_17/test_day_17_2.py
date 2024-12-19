from main_day_17_2 import run_chronospatial_computer


def test_run_chronospatial_computer(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """Register A: 2024
                    Register B: 0
                    Register C: 0

                    Program: 0,3,5,4,3,0"""
    input_file.write_text(input_data)

    result = run_chronospatial_computer(str(input_file))
    print(result)
    assert result == 117440
