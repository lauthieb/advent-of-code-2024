from main_day_10_1 import calculate_tailheads_score


def test_count_distinct_positions(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """89010123
                    78121874
                    87430965
                    96549874
                    45678903
                    32019012
                    01329801
                    10456732"""
    input_file.write_text(input_data)

    result = calculate_tailheads_score(str(input_file))
    print(result)
    assert result == 36
