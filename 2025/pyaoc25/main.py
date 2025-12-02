import argparse
import importlib
import traceback
import logging

from util.input import get_input


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int)
    parser.add_argument("--loglevel", choices=["ERROR", "WARN", "INFO", "DEBUG"])
    parser.add_argument("--skip-a", action="store_true")
    parser.add_argument("--skip-b", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    day_mod = importlib.import_module("days.day%02d" % args.day)
    puzzle = get_input(2025, args.day)
    part_a, part_b = "", ""
    if not args.skip_a:
        try:
            part_a = day_mod.part_a(puzzle)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
    if not args.skip_b:
        try:
            part_b = day_mod.part_b(puzzle)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
    print("Part A: ", part_a)
    print("Part B: ", part_b)


if __name__ == "__main__":
    main()
