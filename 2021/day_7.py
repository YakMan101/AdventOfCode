"""Functions to solve Day-7"""

import statistics


def load_data() -> int:
    """Load in input data and return as list of ints"""

    with open('input.txt') as f:
        return [int(x) for x in f.readline().strip().split(',')]


def calculate_median_position(crabs: list[int]) -> int:
    """
    Return the median value of elements in the crabs list
    """

    return int(round(statistics.median(crabs)))


def calculate_fuel_cost(pos1: int, pos2: int) -> int:
    """Return cost of fuel to move crab from pos1 to pos2"""

    return abs(pos1 - pos2)


def calculate_total_fuel_cost(crabs: list[int], pos: int) -> int:
    """Return total cost of moving all crabs to position 'pos'"""

    return sum([calculate_fuel_cost(x, pos) for x in crabs])


def triangular_number(n: int) -> int:
    """
    Calculate the triangular number for a given n.
    This is the sum of the first n natural numbers: n * (n + 1) // 2
    """

    return n * (n + 1) // 2


def calculate_fuel_cost2(pos1: int, pos2: int) -> int:
    """Return the non-linear cost of fuel to move crab from pos1 to pos2"""

    distance = abs(pos1 - pos2)
    return triangular_number(distance)


def calculate_total_fuel_cost2(crabs: list[int], pos: int) -> int:
    """Return total cost of moving all crabs to position 'pos'"""

    return sum([calculate_fuel_cost2(x, pos) for x in crabs])


def find_optimal_position(crabs: list[int]) -> tuple[int, int]:
    """
    Find the optimal position that minimizes the fuel cost and return it along with the total fuel cost.
    """

    min_pos = min(crabs)
    max_pos = max(crabs)

    min_fuel_cost = float('inf')
    optimal_position = -1

    for pos in range(min_pos, max_pos + 1):
        total_fuel_cost = calculate_total_fuel_cost2(crabs, pos)
        if total_fuel_cost < min_fuel_cost:
            min_fuel_cost = total_fuel_cost
            optimal_position = pos

    return optimal_position, min_fuel_cost


if __name__ == '__main__':

    data = load_data()
    avg_pos = calculate_median_position(data)
    total_fuel = calculate_total_fuel_cost(data, avg_pos)
    print(f'1) {total_fuel}')

    data = load_data()
    optimal_pos, total_fuel = find_optimal_position(data)
    print(f'2) {total_fuel}')
