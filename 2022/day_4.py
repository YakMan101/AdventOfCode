
def load_input() -> list[tuple[str, str]]:
    """Load in input data"""

    with open("input.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        output_data = []

        for line in lines:
            left_right = line.strip().split(',')
            left, right = left_right[0], left_right[1]

            output_data.append((left, right))

        return output_data


def check_overlap(left: str, right: str) -> bool:
    """check if ranges described in string are completely overlapping"""

    left_split = left.split('-')
    left_start, left_end = int(left_split[0]), int(left_split[1])

    right_split = right.split('-')
    right_start, right_end = int(right_split[0]), int(right_split[1])

    if (left_start >= right_start) and (left_end <= right_end):
        return True

    if (left_start <= right_start) and (left_end >= right_end):
        return True

    return False


if __name__ == '__main__':

    data = load_input()
    overlaps = [check_overlap(x[0], x[1]) for x in data]
    total = sum(overlaps)
    print(total)
