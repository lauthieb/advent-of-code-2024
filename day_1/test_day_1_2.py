from main_day_1_2 import calculate_similarity_score


def test_calculate_similarity_score(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    input_file.write_text(input_data)

    result = calculate_similarity_score(str(input_file))
    assert result == 31
