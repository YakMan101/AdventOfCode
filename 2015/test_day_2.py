# pylint: skip-file

import pytest
from day_2 import extract_dimensions, calculate_surface_area, get_shortest_length_around_sides, get_bow_length


@pytest.mark.parametrize("data, result", [('2x3x4', (2, 3, 4)), ('1x1x10', (1, 1, 10)),])
def test_extract_dimensions(data, result):

    assert result == extract_dimensions(data)


@pytest.mark.parametrize("data, result", [((2, 3, 4), 58), ((1, 1, 10), 43),])
def test_calculate_surface_area(data, result):

    assert result == calculate_surface_area(data)


@pytest.mark.parametrize("data, result", [((2, 3, 4), 10), ((1, 1, 10), 4),])
def test_get_shortest_length_around_sides(data, result):

    assert result == get_shortest_length_around_sides(data)


@pytest.mark.parametrize("data, result", [((2, 3, 4), 24), ((1, 1, 10), 10),])
def test_get_bow_length(data, result):

    assert result == get_bow_length(data)
