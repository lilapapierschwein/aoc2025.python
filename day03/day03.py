from pathlib import Path
from typing import override
from utils import Solution


class Day03(Solution):
    def __init__(self) -> None:
        super().__init__(Path(__file__).parent / "input", 3)

    @override
    def get_input(self) -> list[str]:
        with open(self.input_file, "r") as fp:
            text = fp.readlines()
        return [t.strip() for t in text]

    @property
    @override
    def part_one(self) -> int:
        banks: list[list[int]] = []
        total_jolts = 0
        for line in self.get_input():
            banks.append([int(b) for b in line])
        for bank in banks:
            jolts = ""
            first_max_idx = bank.index(max(bank))
            first_max = bank.pop(first_max_idx)
            if first_max_idx == len(bank):
                second_max_idx = bank.index(max(bank))
                second_max = bank.pop(second_max_idx)
                jolts = str(second_max) + str(first_max)
            else:
                second_max_idx = bank.index(max(bank[first_max_idx:]))
                second_max = bank.pop(second_max_idx)
                jolts = str(first_max) + str(second_max)

            total_jolts += int(jolts)
        return total_jolts

    @property
    @override
    def part_two(self) -> int:
        total_jolts: int = 0
        banks: list[list[int]] = []
        for line in self.get_input():
            banks.append([int(b) for b in line])
        for bank in banks:
            jolts = 0
            for i in range(11):
                digit = max(bank[: i - 11])
                bank = bank[bank.index(digit) + 1 :]
                jolts = (jolts * 10) + digit
            jolts = (jolts * 10) + max(bank)
            total_jolts += jolts

        return total_jolts


if __name__ == "__main__":
    print(Day03().part_one)
    print(Day03().part_two)
