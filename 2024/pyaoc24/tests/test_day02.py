from days.day02 import part_a, part_b

EXAMPLE_INPUT="""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def test_part_a():
    out = part_a(EXAMPLE_INPUT)
    assert out == 2

def test_part_b():
    out = part_b(EXAMPLE_INPUT)
    assert out == 4