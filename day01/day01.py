from pathlib import Path
from typing import override


INPUT_FILE = Path(__file__).parent / "input"


class SolutionDay01:
    start_num: int = 50

    def __init__(self, input_file: Path = INPUT_FILE) -> None:
        self.input_file: Path = input_file
        with open(self.input_file, "r") as fp:
            input_lines = fp.readlines()
        self.lines: list[str] = [l.strip() for l in input_lines if l != ""]

    @override
    def __str__(self) -> str:
        return f"AOC 2025 solutions for day 01"

    @property
    def part_one(self) -> int:
        zero_count: int = 0
        cur_num: int = self.start_num

        for line in self.lines:
            rotation = int(line.replace("L", "-").replace("R", ""))
            cur_num = (cur_num + rotation) % 100
            if cur_num == 0:
                zero_count += 1

        return zero_count

    @property
    def part_two(self): ...


if __name__ == "__main__":
    solution = SolutionDay01()
    print(solution)
