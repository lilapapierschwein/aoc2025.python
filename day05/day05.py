from pathlib import Path
from typing import override
import sys

sys.path.insert(1, str(Path(__file__).parent.parent))
from utils import Solution


def get_fresh_ids(low: int, high: int):
    count = low
    while count <= high + 1:
        yield count
        count += 1


class Day05(Solution):
    def __init__(self) -> None:
        super().__init__(Path(__file__).parent / "input", 5)

    @override
    def get_input(self) -> list[str]:
        with open(
            self.input_file,
            "r",
        ) as fp:
            text = fp.readlines()
        return text

    @property
    @override
    def part_one(self) -> int:
        input = self.get_input()
        ranges = [list(map(int, line.split("-"))) for line in input if "-" in line]
        numbers = [int(line) for line in input if not "-" in line]
        fresh_count: int = 0

        for num in numbers:
            for r in ranges:
                if r[0] <= num <= r[1]:
                    fresh_count += 1
                    break

        return fresh_count

    @property
    @override
    def part_two(self) -> object:
        return super().part_two


if __name__ == "__main__":
    print(Day05().part_one)
    print(Day05().part_two)
