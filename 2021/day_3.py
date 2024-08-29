"""Functions to solve Day-3"""

import numpy as np


def load_input() -> list[int]:
    """Return input data"""
    
    with open("input.txt", "r", encoding="utf-8") as f:
        return np.array([[int(z) for z in list(x.strip())] for x in f.readlines()])


def calculate_power(lines: np.ndarray[list[int]]):
    """Calculate gamma and epsilon properties of the submarine"""

    counts_zero = np.sum(lines == 0, axis=0)
    counts_one = np.sum(lines == 1, axis=0)

    gamma = int(''.join(['0' if x > y else '1' for x, y in zip(counts_zero, counts_one)]), 2)
    epsilon = int(''.join(['0' if x < y else '1' for x, y in zip(counts_zero, counts_one)]), 2)

    return gamma, epsilon


def life_support(lines: np.ndarray):
    """Calculate life support rating for the submarine based on oxygen generator and CO2 scrubber ratings."""
    
    lines_oxy, lines_co2 = lines.copy(), lines.copy()

    for i in range(lines.shape[1]):
        if len(lines_oxy) > 1:
            counts_zero = np.sum(lines_oxy[:, i] == 0)
            counts_one = np.sum(lines_oxy[:, i] == 1)
            most = 1 if counts_one >= counts_zero else 0

            lines_oxy = lines_oxy[lines_oxy[:, i] == most]
        
        if len(lines_co2) > 1:
            counts_zero = np.sum(lines_co2[:, i] == 0)
            counts_one = np.sum(lines_co2[:, i] == 1)
            least = 0 if counts_zero <= counts_one else 1

            lines_co2 = lines_co2[lines_co2[:, i] == least]
    
    oxy = int(''.join(map(str, lines_oxy[0])), 2)
    co2 = int(''.join(map(str, lines_co2[0])), 2)

    return oxy, co2, 



if __name__ == '__main__':

    example_data = np.array([
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        ])
    
    data = load_input()
    
    # Part 1
    gamma, epsilon = calculate_power(data)
    print('1)', gamma*epsilon)

    # Part 2
    oxy, co2 = life_support(data)
    print('2)', oxy*co2)