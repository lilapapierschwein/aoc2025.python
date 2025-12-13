from pathlib import Path
from typing import override
import re
from utils import Solution


RX_ROLL_MARKER = re.compile(r"@")


def find_rolls(row: str, rx_roll: re.Pattern[str] = RX_ROLL_MARKER):
    return [m.start() for m in list(re.finditer(rx_roll, row))]


def count_accessible_rolls(
    rolls_cur_row: list[int], rolls_prev_row: list[int], rolls_next_row: list[int]
):
    accessible_rolls = 0

    for roll in rolls_cur_row:
        adj_rolls = 0
        for i in range(roll - 1, roll + 2):
            if i in rolls_prev_row:
                adj_rolls += 1
            if i in rolls_next_row:
                adj_rolls += 1
        if roll - 1 in rolls_cur_row:
            adj_rolls += 1
        if roll + 1 in rolls_cur_row:
            adj_rolls += 1
        if adj_rolls < 4:
            accessible_rolls += 1

    return accessible_rolls


def remove_accessible_rows(
    rolls_cur_row: list[int], rolls_prev_row: list[int], rolls_next_row: list[int]
):
    inaccessible_rolls: list[int] = []
    removed_rolls: list[int] = []

    for roll in rolls_cur_row:
        adj_rolls = 0
        for i in range(roll - 1, roll + 2):
            if i in rolls_prev_row:
                adj_rolls += 1
            if i in rolls_next_row:
                adj_rolls += 1
        if roll - 1 in rolls_cur_row:
            adj_rolls += 1
        if roll + 1 in rolls_cur_row:
            adj_rolls += 1

        if adj_rolls >= 4:
            inaccessible_rolls.append(roll)
        else:
            removed_rolls.append(roll)

    return inaccessible_rolls, removed_rolls


class Day04(Solution):
    def __init__(self) -> None:
        super().__init__(Path(__file__).parent / "input", 4)

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
        rows = [find_rolls(line) for line in input]
        total_accessible: int = 0
        for row_id, row in enumerate(rows):
            prev_row = [] if row_id == 0 else rows[row_id - 1]
            next_row = [] if row_id == len(rows) - 1 else rows[row_id + 1]

            accessible_rolls = count_accessible_rolls(row, prev_row, next_row)
            total_accessible += accessible_rolls

        return total_accessible

    @property
    @override
    def part_two(self) -> int:
        input = self.get_input()
        rows = [find_rolls(line) for line in input]
        total_removed: int = 0
        while True:
            rolls_removed: int = 0
            new_rows: list[list[int]] = []
            for row_id, row in enumerate(rows):
                prev_row = [] if row_id == 0 else rows[row_id - 1]
                next_row = [] if row_id == len(rows) - 1 else rows[row_id + 1]

                inaccessible_rolls, removed_rolls = remove_accessible_rows(
                    row, prev_row, next_row
                )
                new_rows.append(inaccessible_rolls)
                rolls_removed += len(removed_rolls)
            if rolls_removed > 0:
                total_removed += rolls_removed
                rows = new_rows
                continue
            else:
                break
        return total_removed


if __name__ == "__main__":
    print(Day04().part_one)
    print(Day04().part_two)
