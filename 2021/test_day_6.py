import pytest

from day_6 import spawn_fish, go_next_day, simulate_fish_life


@pytest.mark.parametrize("test_list, expected", [([0, 0, 0], [0, 0, 0]),
                                                 ([-1, 0, 1], [6, 0, 1, 8]),
                                                 ([-1, -1, -1], [6, 6, 6, 8, 8, 8])])
def test_spawn_fish(test_list, expected):

    res = spawn_fish(test_list)
    assert res == expected


@pytest.mark.parametrize("test_list, expected", [([0, 0, 0], [-1, -1, -1]),
                                                 ([2, 3, 2], [1, 2, 1]),
                                                 ([50000, 40, 21], [49999, 39, 20])])
def test_go_next_day(test_list, expected):
    res = go_next_day(test_list)
    assert res == expected


@pytest.mark.parametrize("test_list, days, expected", [([3, 4, 3, 1, 2], 18, 26),
                                                       ([3, 4, 3, 1, 2], 80, 5934)])
def test_simulate_fish_life(test_list, days, expected):

    total_fish = simulate_fish_life(test_list, days)

    assert total_fish == expected
