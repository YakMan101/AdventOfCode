"""Functions to solve Day-2"""


def load_input() -> list[int]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        return ([x.strip() for x in f.readlines()])


def calculate_position(commands: list[str]) -> int:
    """
    Return final position relative to origin
    """

    pos_depth = pos_horizontal = 0
    for command in commands:
        c = command.split(' ')
        dire, dist = c[0], int(c[1])

        if dire == 'forward':
            pos_horizontal += int(dist)
        else:
            pos_depth += int(dist) * -1 if dire == 'up' else int(dist)

    return pos_horizontal, pos_depth


def calculate_position_with_aim(commands: list[str]) -> int:
    """
    Return final position relative to origin accounting for aim
    """

    pos_depth = pos_horizontal = aim = 0
    for command in commands:
        c = command.split(' ')
        dire, dist = c[0], int(c[1])

        if dire == 'forward':
            pos_horizontal += dist
            pos_depth += aim * dist
        else:
            aim += dist * -1 if dire == 'up' else dist

    return pos_horizontal, pos_depth


if __name__ == '__main__':

    comm = load_input()

    # Part 1
    pos_h, pos_d = calculate_position(comm)
    print('1)', pos_h*pos_d)

    # Part 2
    pos_h, pos_d = calculate_position_with_aim(comm)
    print('2)', pos_h*pos_d)
