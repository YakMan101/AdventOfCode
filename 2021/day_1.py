"""Functions to solve Day-1"""

def load_input() -> list[int]:
    """Return input data"""
    with open("input.txt", "r", encoding="utf-8") as f:
        return([int(x.strip()) for x in f.readlines()])

def count_increased_depth_measurements(m: list[int]) -> int:
    """
    Count the number of times a depth measurement increases 
    from the previous measurement.
    """

    return len([x for x in range(1, len(m)) if m[x] > m[x-1]])

def count_increased_depth_measurements_sliding_window(m: list[int]) -> int:
    """
    Count the number of times the sum of measurements 
    within a three-measurement sliding window increases 
    compared to the previous window's sum.
    """

    return len([x for x in range(3, len(m)) if sum(m[x-2:x+1]) > sum(m[x-3:x])])

if __name__ == '__main__':

    measurements = load_input()

    # Part 1
    print('1)', count_increased_depth_measurements(measurements))

    # Part 2
    print('2)',count_increased_depth_measurements_sliding_window(measurements))