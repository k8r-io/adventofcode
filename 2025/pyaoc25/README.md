# Advent of Code 2025: Python
## Run solution

```shell
uv run main.py --day <int>
```
This will attempt to run the day's solution, first fetching the puzzle input if needed. The puzzle inputs get cached in
the "./cache" directory and will be automatically pulled if that day's input is not already cached.

To make the auto-fetch work, make sure you have a .token file in your current working directory that contains the
session ID from your cookies for https://adventofcode.com/


### Addtional options

You can skip running parts of the solution if needed with the `--skip-a` and `--skip-b` flags. 

Also, the `--loglevel` flag can be used to adjust the logger.

## Run tests
The project isn't structured like a module, so run pytest as a module to ensure the PYTHON_PATH gets mangled
appropriately.

```shell
uv run python3 -m pytest
```