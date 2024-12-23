from main_day_23_2 import calculate_lan_party_password


def test_calculate_lan_party_password(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """kh-tc
                    qp-kh
                    de-cg
                    ka-co
                    yn-aq
                    qp-ub
                    cg-tb
                    vc-aq
                    tb-ka
                    wh-tc
                    yn-cg
                    kh-ub
                    ta-co
                    de-co
                    tc-td
                    tb-wq
                    wh-td
                    ta-ka
                    td-qp
                    aq-cg
                    wq-ub
                    ub-vc
                    de-ta
                    wq-aq
                    wq-vc
                    wh-yn
                    ka-de
                    kh-ta
                    co-tc
                    wh-qp
                    tb-vc
                    td-yn"""
    input_file.write_text(input_data)

    result = calculate_lan_party_password(str(input_file))
    print(result)
    assert result == "co,de,ka,ta"
