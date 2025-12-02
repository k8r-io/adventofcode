import pytest
from days.day02 import part_a_is_valid, part_a, part_b, part_b_is_valid


@pytest.fixture
def test_puzzle() -> str:
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


@pytest.mark.parametrize(
    "num,ans",
    [
        (123123, False),
        (101, True),
        (55, False),
    ],
)
def test_part_a_is_valid(num: int, ans: bool):
    assert part_a_is_valid(num) is ans


def test_part_a(test_puzzle: str):
    assert part_a(test_puzzle) == 1227775554


@pytest.mark.parametrize(
    "num,ans",
    [
        (123123, False),
        (101, True),
        (55, False),
        (12341234, False),
        (123123123, False),
        (1212121212, False),
        (1111111, False),
    ],
)
def test_part_b_is_valid(num: int, ans: bool):
    assert part_b_is_valid(num) is ans


def test_part_b(test_puzzle: str):
    assert part_b(test_puzzle) == 4174379265
