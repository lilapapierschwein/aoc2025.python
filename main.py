#!/usr/bin/env python3

from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04
from utils import Solution

solutions: list[Solution] = [Day01(), Day02(), Day03(), Day04()]


def show_solution(solution: Solution) -> None:
    print(solution, end="\n\n")
    print("Part One:", solution.part_one)
    print("Part Two:", solution.part_two)


def main() -> None:
    for i, solution in enumerate(solutions):
        show_solution(solution)
        if i < len(solutions) - 1:
            print("-" * 80)


if __name__ == "__main__":
    main()
