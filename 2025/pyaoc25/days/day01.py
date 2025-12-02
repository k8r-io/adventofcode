import math
import logging
from typing import Tuple

DIAL_WIDTH = 100


def part_a(puzzle: str) -> str:
    current = 50
    password = 0
    logger = logging.getLogger(__name__)
    logger.debug(f"Starting at {current}")
    for line in puzzle.splitlines():
        current, score = part_a_step(current, line)
        password += score
        logger.debug(f"{line}: {current}")

    return str(password)


def part_a_step(current: int, move: str) -> Tuple[int, int]:
    direction = move[0]
    distance = int(move[1:])
    dir_val = 1 if direction == "R" else -1
    current = (current + dir_val * distance) % DIAL_WIDTH
    score = 1 if current == 0 else 0
    return current, score


def part_b(puzzle: str) -> str:
    current = 50
    password = 0

    logger = logging.getLogger(__name__)
    logger.debug(f"Starting at {current}")
    for line in puzzle.splitlines():
        previous = current
        current, score = part_b_step(current, line)
        password += score
        logger.debug(
            f"{previous} + {line} -> {current} | {password}{'(+'+str(score)+')' if score else ''}"
        )

    return str(password)


def part_b_step(current: int, move: str) -> Tuple[int, int]:
    # (L|R)\d+
    direction = move[0].upper()
    distance = int(move[1:])
    previous = current
    dir_val = 1 if direction == "R" else -1
    current += dir_val * distance

    score = 0
    if direction == "R" and current >= DIAL_WIDTH:
        score += math.floor(current / DIAL_WIDTH)
    elif direction == "L" and current <= 0:
        score += abs(math.ceil(current / DIAL_WIDTH))
        if previous > 0:
            score += 1

    current = current % DIAL_WIDTH
    return current, score
