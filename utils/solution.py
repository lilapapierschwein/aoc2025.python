from pathlib import Path
from typing import override


class Solution:
    def __init__(self, input_file: Path, day: int) -> None:
        self.input_file: Path = input_file
        self.day: int = day

    @override
    def __str__(self) -> str:
        return f"Advent of Code 2025 - Python solutions for day {self.day}"

    def get_input(self) -> object: ...

    @property
    def part_one(self) -> object: ...

    @property
    def part_two(self) -> object: ...
