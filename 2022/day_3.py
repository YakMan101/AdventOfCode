"""Functions to solve Day-3"""

def load_input(filename: str) -> list[int]:
    """Return input data"""

    with open(filename, "r", encoding="utf-8") as f:
        return([x.strip() for x in f.readlines()])
    

def get_rucksack_compartments(line: list[str]) -> list[str]:
    """Return two equal sized rucksack string as a list"""

    return line[:len(line)//2], line[len(line)//2:]

def get_all_rucksack_compartments(lines: list[str]) -> list[str]:
    """Return two equal sized rucksack string as a list"""

    left, right = [], []
    for line in lines:
        comp1, comp2 = get_rucksack_compartments(line)
        left.append(comp1),
        right.append(comp2)

    return left, right


def get_misplaced_letter(comp1: str, comp2: str) -> str:
    """Return misplaced letter"""

    for char in comp1:
        if char in comp2:
            return char
    
    return None

def calculate_priority(char: str) -> int:
    """Convert string into corresponding int value"""

    priority = ord(char) - 96 if char.islower() else ord(char) - 38
    return priority



if __name__ == '__main__':
    data = load_input('input.txt')

    # Part 1
    comp1, comp2 = get_all_rucksack_compartments(data)
    misplaced_letters = [get_misplaced_letter(x1, x2) for x1, x2 in zip(comp1, comp2)]
    prios = [calculate_priority(x) for x in misplaced_letters]
    print('1)', sum(prios))