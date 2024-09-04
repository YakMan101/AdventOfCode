"""Functions to solve Day-5"""


def load_input() -> tuple[list[int], list[list[list[int]]]]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        coords = []
        max_number = 0
        for line in f.readlines():
            start, end = tuple(line.split(' -> '))
            start_x, start_y = tuple([int(x) for x in start.split(',')])
            end_x, end_y = tuple([int(x) for x in end.split(',')])

            temp_max = max(start_x, start_y, end_x, end_y)
            max_number = temp_max if temp_max > max_number else max_number

            coords.append(((start_x, start_y), (end_x, end_y)))
        return coords, max_number


def create_grid(size: int):
    """Create grid to keep track of lines and intersections"""

    return [[0 for _ in range(size)] for _ in range(size)]


def draw_line_on_grid(grid: list[list[int]],
                      start: tuple[int, int],
                      end: tuple[int, int]) -> None:
    """
    Add 1 to each number in the line 
    fixed by coordinates of 'start' and 'end'
    """

    if start[0] == end[0]:  # vertical line
        y_start, y_end = sorted([start[1], end[1]])
        for i in range(y_start, y_end + 1):
            grid[i][start[0]] += 1

    elif start[1] == end[1]:  # horizontal line
        x_start, x_end = sorted([start[0], end[0]])
        for i in range(x_start, x_end + 1):
            grid[start[1]][i] += 1

    else:  # diagonal line (45-degree lines only)
        pass


def draw_line_on_grid2(grid: list[list[int]],
                       start: tuple[int, int],
                       end: tuple[int, int]) -> None:
    """
    Add 1 to each number in the line 
    fixed by coordinates of 'start' and 'end'
    """

    if start[0] == end[0]:  # vertical line
        y_start, y_end = sorted([start[1], end[1]])
        for i in range(y_start, y_end + 1):
            grid[i][start[0]] += 1

    elif start[1] == end[1]:  # horizontal line
        x_start, x_end = sorted([start[0], end[0]])
        for i in range(x_start, x_end + 1):
            grid[start[1]][i] += 1

    else:  # diagonal line (45-degree lines only)
        x_step = 1 if end[0] > start[0] else -1
        y_step = 1 if end[1] > start[1] else -1

        x, y = start
        while (x, y) != (end[0] + x_step, end[1] + y_step):
            grid[y][x] += 1
            x += x_step
            y += y_step


def count_intersections(grid: list[list[int]]) -> int:
    """Count the number of elements with value of 2 or greater"""

    count = 0
    for row in grid:
        for val in row:
            if val >= 2:
                count += 1

    return count


if __name__ == '__main__':
    coords, maxi = load_input()
    grid = create_grid(maxi+1)

    # Part 1
    for coord in coords:
        draw_line_on_grid(grid, coord[0], coord[1])

    print(f'1) {count_intersections(grid)}')

    grid = create_grid(maxi+1)

    # Part 2
    for coord in coords:
        draw_line_on_grid2(grid, coord[0], coord[1])

    print(f'2) {count_intersections(grid)}')
