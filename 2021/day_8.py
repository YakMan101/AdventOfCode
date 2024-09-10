"""Functions to solve Day-8"""

UNIQUE_NUMBERS_DICT = {  # number of segments for digit display
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def load_data() -> tuple[list[list[str]], list[list[str]]]:
    """Read input.txt and return submarine display inputs and outputs"""

    with open('input.txt', 'r+', encoding='utf-8') as f:
        inputs, outputs = [], []
        for line in f.readlines():
            left_right = line.split('|')
            inputs.append(left_right[0].strip().split())
            outputs.append(left_right[1].strip().split())

        return inputs, outputs


def count_unique_numbers(line: list[str]) -> int:
    """
    Count the number of strings that correspond 
    to a digit with a unique number of segments
    """

    total = 0
    for str in line:
        if UNIQUE_NUMBERS_DICT.get(len(str)):
            total += 1

    return total


if __name__ == '__main__':

    input_data, output_data = load_data()

    # Part 1
    total_unique_numbers = sum([count_unique_numbers(x) for x in output_data])
    print(f'1) {total_unique_numbers}')
