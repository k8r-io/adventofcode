from typing import List

from util.input import transform_input


def parse_reports(puzzle_input: str) -> List[List[int]]:
    grid: List[List[int]] = []
    for line in puzzle_input.splitlines():
        new_line = [ int(l) for l in line.split(" ") ]
        grid.append(new_line)
    return grid


@transform_input(parse_reports)
def part_a(*grid: List[int]) -> int:
    return check_safety(grid, 0)

def check_safety(grid: List[List[int]], error_limit: int=0) -> int:
    safe_count = 0
    for line in grid:
        sort_dir = 0
        error_count = 0
        for i in range(len(line)-1):
            diff = line[i]-line[i+1]
            if  abs(diff) < 1 or abs(diff) > 3 :
                error_count += 1
                break
            cur_dir = diff / abs(diff)
            if sort_dir == 0:
                sort_dir = cur_dir
            if sort_dir != cur_dir:
                error_count += 1
                break
        if error_count <= error_limit:
            safe_count+=1
    return safe_count


@transform_input(parse_reports)
def part_b(*grid: List[int]) -> int:
    return check_safety(grid, 1)