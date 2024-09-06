
import pytest

from day_7 import *


def test_load_data():

    data = load_data()
    assert isinstance(data, list) == True
    assert isinstance(data[0], int) == True


@pytest.mark.parametrize("list_pos, average", [([1, 2, 3], 2),
                                               ([0, 0, 0], 0),
                                               ([2, 1], 2),
                                               ([2, 1, 1], 1)])
def test_calculate_average_position(list_pos, average):

    assert calculate_median_position(list_pos) == average


@pytest.mark.parametrize("pos1, pos2, cost", [(16, 2, 14),
                                              (1, 2, 1),
                                              (14, 2, 12)])
def test_calculate_fuel_cost(pos1, pos2, cost):

    assert calculate_fuel_cost(pos1, pos2) == cost


@pytest.mark.parametrize("crabs, pos, total_fuel", [([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2, 37),
                                                    ([1, 1, 0], 1, 1)])
def test_calculate_total_fuel_cost(crabs, pos, total_fuel):

    assert calculate_total_fuel_cost(crabs, pos) == total_fuel


def test_load_data():
    data = load_data()
    assert isinstance(data, list)
    assert isinstance(data[0], int)


@pytest.mark.parametrize("list_pos, median", [([1, 2, 3], 2),
                                              ([0, 0, 0], 0),
                                              ([2, 1], 2),
                                              ([2, 1, 1], 1)])
def test_calculate_median_position(list_pos, median):
    assert calculate_median_position(list_pos) == median


@pytest.mark.parametrize("pos1, pos2, cost", [(16, 5, 66),
                                              (1, 5, 10),
                                              (2, 5, 6)])
def test_calculate_fuel_cost2(pos1, pos2, cost):
    assert calculate_fuel_cost2(pos1, pos2) == cost


@pytest.mark.parametrize("crabs, pos, total_fuel", [([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 5, 168),
                                                    ([1, 1, 0], 1, 1)])
def test_calculate_total_fuel_cost2(crabs, pos, total_fuel):
    assert calculate_total_fuel_cost2(crabs, pos) == total_fuel


def test_find_optimal_position():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    optimal_pos, total_fuel = find_optimal_position(crabs)
    assert optimal_pos == 5
    assert total_fuel == 168
