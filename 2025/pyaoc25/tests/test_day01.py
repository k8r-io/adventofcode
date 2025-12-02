from days.day01 import part_a, part_b, part_b_step
import pytest


@pytest.fixture
def test_puzzle() -> str:
    return """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_day01_part_a(test_puzzle: str):
    res = part_a(test_puzzle)
    assert "3" == res


def test_day01_part_b(test_puzzle: str):
    res = part_b(test_puzzle)
    assert "6" == res


@pytest.mark.parametrize(
    "start_pos,move,expected_pos,expected_score",
    [
        (50, "L50", 0, 1),
        (50, "L51", 99, 1),
        (50, "R49", 99, 0),
        (50, "R51", 1, 1),
        (50, "R251", 1, 3),
        (0, "R1", 1, 0),
        (0, "R100", 0, 1),
        (0, "R500", 0, 5),
    ],
)
def test_part_b_step(start_pos, move, expected_pos, expected_score):
    current, score = part_b_step(start_pos, move)
    assert expected_pos == current
    assert expected_score == score
