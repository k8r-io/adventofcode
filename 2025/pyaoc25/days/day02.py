import math
from typing import Callable


def do_puzzle(puzzle: str, valid: Callable) -> int:
    ans = 0
    ranges = puzzle.split(",")
    for cur in ranges:
        low, high = cur.split("-", 1)
        low = int(low)
        high = int(high)
        for num in range(low, high + 1):
            if not valid(num):
                ans += num
    return ans


def part_a(puzzle: str) -> int:
    return do_puzzle(puzzle, part_a_is_valid)


def part_a_is_valid(num: int) -> bool:
    num_str = str(num)
    midpoint = math.floor(len(num_str) / 2)
    return num_str[:midpoint] != num_str[midpoint:]


def part_b(puzzle: str) -> int:
    return do_puzzle(puzzle, part_b_is_valid)


def part_b_is_valid(num: int) -> bool:
    num_str = str(num)
    halflen = math.floor(len(num_str) / 2)
    for cur in range(1, halflen + 1):
        parts = [num_str[i : cur + i] for i in range(0, len(num_str), cur)]
        first = parts[0]
        if all(p == first for p in parts):
            return False
    return True
