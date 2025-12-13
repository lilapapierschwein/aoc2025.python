from pathlib import Path
from typing import override
from utils import Solution


class Day02(Solution):
    def __init__(self) -> None:
        super().__init__(Path(__file__).parent / "input", 2)

    @override
    def get_input(self) -> str:
        with open(self.input_file, "r") as fp:
            text = fp.read().strip()
        return text

    @property
    @override
    def part_one(self) -> int:
        ranges = [list(map(int, r.split("-"))) for r in self.get_input().split(",")]
        invalid_ids: list[int] = []
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                num_str = str(i)
                if len(num_str) % 2 != 0:
                    continue
                if num_str[: len(num_str) // 2] == num_str[len(num_str) // 2 :]:
                    invalid_ids.append(i)
        return sum(invalid_ids)

    @property
    @override
    def part_two(self) -> int:
        ranges = [list(map(int, r.split("-"))) for r in self.get_input().split(",")]
        invalid_ids: list[int] = []
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                if self.is_invalid(str(i)):
                    invalid_ids.append(i)

        return sum(invalid_ids)

    def is_invalid(self, num_str: str) -> bool:
        is_invalid = False
        num_len: int = len(num_str)
        if num_len < 2:
            pass
        elif num_str.count(num_str[0]) == num_len:
            is_invalid = True
        else:
            for c in range(2, len(num_str) // 2 + 1):
                if num_len % c == 0:
                    if num_str.count(num_str[: num_len // c]) == c:
                        is_invalid = True
                        break

        return is_invalid


if __name__ == "__main__":
    print(Day02().part_two)
