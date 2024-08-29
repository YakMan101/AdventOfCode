"""Functions to solve Day-2"""


def load_input() -> list[int]:
    """Return input data"""

    with open("input.txt", "r", encoding="utf-8") as f:
        return ([x.strip() for x in f.readlines()])


def extract_dimensions(string: str) -> tuple[int, int, int]:
    """Convert string into tuple of dimensions (length, width, height)"""

    return tuple([int(x) for x in string.split('x')])


def calculate_surface_area(dim: tuple[int, int, int]) -> int:
    """Calculate square feet of wrapping paper required plus slack"""

    sa1, sa2, sa3 = dim[0]*dim[1], dim[1]*dim[2], dim[2]*dim[0]
    return min([sa1, sa2, sa3]) + 2*(sa1 + sa2 + sa3)


def get_shortest_length_around_sides(dim: tuple[int, int, int]) -> int:
    """Return the shortest perimeter around the present sides"""

    sorted_dims = sorted(dim)
    return 2 * (sorted_dims[0] + sorted_dims[1])


def get_bow_length(dim: tuple[int, int, int]) -> int:
    """Return length of bow which is equal to volume of present"""

    return dim[0] * dim[1] * dim[2]


if __name__ == '__main__':

    dims = load_input()

    # Part 1
    dimensions = [extract_dimensions(x) for x in dims]
    surface_areas = [calculate_surface_area(x) for x in dimensions]
    print('1)', sum(surface_areas), 'ft^2')

    # Part 2
    total_ribbon = [get_shortest_length_around_sides(x) + get_bow_length(x)
                    for x in dimensions]
    print(total_ribbon)
    print('1)', sum(total_ribbon), 'ft')
