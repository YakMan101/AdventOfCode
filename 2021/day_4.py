"""Functions to solve Day-4"""


def load_input() -> tuple[list[int], list[list[list[int]]]]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        numbers = [int(x) for x in lines[0].strip().split(',')]
        tables = []
        table_index = 0
        for line in lines[2:]:
            if not line.strip():
                table_index += 1

            else:
                if len(tables) != table_index + 1:
                    tables.append([])
                tables[table_index].append([int(x)
                                            for x in line.strip().split()])
        return numbers, tables


def create_table_mask(table: list[list[int]]):
    """Return mask of a given table filled with False"""

    mask = [[False for _ in row] for row in table]
    return mask


def flip_mask(table: list[list[int]], mask: list[list[bool]], number: int) -> None:
    """update table mask if there is a number match"""

    for row in range(len(table)):
        for col in range(len(table[0])):
            if table[row][col] == number:
                mask[row][col] = True


def check_mask_rows(mask: list[list[bool]]) -> None:
    """Check if any rows of the mask are all 'True'"""

    if any(all(x for x in row) for row in mask):
        return True

    return False


def check_mask_cols(mask: list[list[bool]]) -> None:
    """Check if any columns of the mask are all 'True'"""

    if any(all(mask[i][j] for i in range(len(mask))) for j in range(len(mask[0]))):
        return True

    return False


def print_table(table: list[list[int]]) -> None:
    """Print table in pretty manner"""

    for row in table:
        print(' '.join([str(x) for x in row]))


def calculate_score(table: list[list[int]], mask: list[list[bool]]) -> int:
    total = 0

    for row in range(len(table)):
        for col in range(len(table[0])):
            if not mask[row][col]:
                total += table[row][col]

    return total


if __name__ == '__main__':
    bn, t = load_input()

    # Part 1
    masks = [create_table_mask(x) for x in t]
    table_found = False

    for i, number in enumerate(bn):
        for table, mask in zip(t, masks):
            flip_mask(table, mask, number)
            if check_mask_rows(mask) or check_mask_cols(mask):
                score = calculate_score(table, mask)
                print(
                    f'1) table {t.index(table) + 1} wins,\nnumbers:{bn[:i+1]}:')
                print(f'Total score: {score}x{number}={score*number}')
                table_found = True
                break

        if table_found:
            break

    # Part 2
    masks = [create_table_mask(x) for x in t]
    tables_indices = list(range(len(t)))
    table_found = False

    for number in bn:
        tables_to_remove = []

        for i, index in enumerate(tables_indices):
            table, mask = t[index], masks[index]
            flip_mask(table, mask, number)

            if check_mask_rows(mask) or check_mask_cols(mask):
                if len(tables_indices) > 1:
                    tables_to_remove.append(index)
                else:
                    score = calculate_score(
                        t[tables_indices[0]], masks[tables_indices[0]])
                    print(f'2) table {tables_indices[0] + 1} is last to win')
                    print(f'Total score: {score}x{number}={score * number}')
                    table_found = True
                    break

        for index in tables_to_remove:
            tables_indices.remove(index)

        if table_found:
            break
