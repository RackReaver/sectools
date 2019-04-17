import os

import csv_tools

import_csv_content = """row_1_1,
                        row_1_2,
                        row_1_3,
                        row_1_4,
                        row_1_5
                        \n
                        row_2_1,
                        row_2_2,
                        row_2_3,
                        row_2_4,
                        row_2_5
                        \n
                        row_3_1,
                        row_3_2,
                        row_3_3,
                        row_3_4,
                        row_3_5
                        \n
                        row_4_1,
                        row_4_2,
                        row_4_3,
                        row_4_4,
                        row_4_5
                        \n
                        """


def test_import_csv_with_titles(tmp_path):
    """Testing the input value against the return value"""
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_import_csv.csv"
    p.write_text(import_csv_content)
    titles, data = csv_tools.import_csv(p, titles=True)

    assert type(titles) == tuple
    assert type(data) == tuple
    # TODO: write asserts to check data validity