"""Functions to solve Day-4"""


def load_input() -> list[int]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        return ([x.strip() for x in f.readlines()])


