from pathlib import Path
from typing import override
from utils import Solution


class Day01(Solution):
    def __init__(self) -> None:
        super().__init__(Path(__file__).parent / "input", 1)
        self.start_num: int = 50

    @override
    def get_input(self) -> list[str]:
        with open(self.input_file, "r") as fp:
            lines = fp.readlines()
        return lines

    @property
    @override
    def part_one(self) -> int:
        lines = self.get_input()
        zero_count: int = 0
        cur_num: int = self.start_num

        for line in lines:
            rotation = int(line.replace("L", "-").replace("R", ""))
            cur_num = (cur_num + rotation) % 100
            if cur_num == 0:
                zero_count += 1

        return zero_count

    @property
    @override
    def part_two(self): ...
