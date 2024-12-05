from main_day_5_1 import count_middle_page_number


def test_count_middle_page_number(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """47|53
                    97|13
                    97|61
                    97|47
                    75|29
                    61|13
                    75|53
                    29|13
                    97|29
                    53|29
                    61|53
                    97|53
                    61|29
                    47|13
                    75|47
                    97|75
                    47|61
                    75|61
                    47|29
                    75|13
                    53|13

                    75,47,61,53,29
                    97,61,53,29,13
                    75,29,13
                    75,97,47,61,53
                    61,13,29
                    97,13,75,29,47"""
    input_file.write_text(input_data)

    result = count_middle_page_number(str(input_file))
    print(result)
    assert result == 143
